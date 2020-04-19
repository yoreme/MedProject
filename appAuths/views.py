from django.shortcuts import render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model,authenticate, login, logout
from django.contrib.auth.models import update_last_login
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.utils import timezone

from django.core import mail

from rest_framework import authentication,serializers,status,generics,permissions

from rest_framework.permissions import AllowAny,IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (LoginSerializer,LogoutSerializer,PasswordChangeSerializer,
RegistrationSerializer,PasswordResetSerializer,PasswordResetConfirmSerializer,UserSerializer)

from .models import User,UserProfile
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.




class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    #renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """ Post method for registration  """
        logger.info('Registration request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            logger.info('Serializer value:{}'.format(serializer.validated_data))
            email= serializer.validated_data['email']
            password= serializer.validated_data['password']
            logger.info('Serializer validated email value:{}'.format(email))
            serializer.save(is_verified = True)
            resp={
                    'status':'00',
                    'message':'user registration was successfully',
                    'data':'null'
                }
                #serializer.data
            return Response(resp, status=status.HTTP_201_CREATED)
        return Response({'message':'An error occurred while processing yur request','error':serializer.errors,'data':'null'}, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    permission_classes=[AllowAny,]
    serializer_class=LoginSerializer

    def post(self,request):
        """ Post method to get login  """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            logger.info('login detail email:{} password:{}'.format(email,password))

            #we might want user to login with either email or username letter
            if not '@' in email:
                try:
                    logger.info('in if is username value {}'.format(email))
                    email = User.objects.get(username=email).email
                    logger.info('email value:{}'.format(email))
                except User.DoesNotExist:
                    return Response({'message': "Invalid credentials", 'status': '00','data':'null'},status=status.HTTP_400_BAD_REQUEST)
            else:
                pass 

            logger.info('login authenticate user_searchvalue:{}'.format(email))
            user = authenticate(username=email,password=password)
            if user is not None:
                if not user.is_active:
                    return Response({'message': "Validation Error", 'status': '00','errors':'This user has been deactivated.','data':'null'},status=status.HTTP_400_BAD_REQUEST)
                if not user.is_verified:
                    return Response({'message': "Validation Error", 'status': '00','errors':'This user has a pending email confimation!.','data':'null'},status=status.HTTP_400_BAD_REQUEST)
                try:
                    logger.info('login successful for {}'.format(email))
                    #update user and userprofile 
                    update_last_login(None,user)
                    UserProfile.objects.filter(user=user).update(available_online = True)
                except Exception as e:
                    logger.error('an error ocurred while updae user and user profile in login, info : {} '.format(e))

                resp={
                    'status':'00',
                    'message':'user login was successfully',
                    'data':{
                        'token': user.token,
                        'firstname':user.first_name,
                        'lastname':user.last_name,
                        'email':user.email
                    }
                }
                return Response(resp, status=status.HTTP_200_OK)
            else:
               msgdetail=serializer.errors
               return Response({'message': "Invalid credentials", 'status': '400','errors':f"{msgdetail}",'data':'null'},status=status.HTTP_400_BAD_REQUEST) 

        else:
            msgdetail=serializer.errors
            return Response({'message': "Invalid credentials", 'status': '400','errors':f"{msgdetail}",'data':'null'},status=status.HTTP_400_BAD_REQUEST)


class ManageUserView(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=(IsAuthenticated,)

    def get_object(self):
        """ Retrieve the current authenticted user"""
        resp={
                'status':'00',
                'message':'user details retrieved successfully',
                'data': self.request.user
            }
        return Response(resp, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    """
    Logs out an authorized user.
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        logger.info('Logout request data:{}'.format(request.data))
        user = User.objects.get(email=request.user.email)
        UserProfile.objects.filter(user=user).update(available_online=False)
        logout(request)
        return Response({'message': "Successfully logged out", 'status': '00','data':'null'},status=status.HTTP_200_OK)



class ChangePasswordAPIView(APIView):
    """
    Endpoint to Modified an authorize use password.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer
    def post(self, request):
        logger.info('Change Password request data:{}'.format(request.data))
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #check user password
            password=serializer.validated_data['new_password']
            user = request.user
            logger.info('Change Password request user:{}'.format(user))
            if user.check_password(password):
                return Response({'message': "Validation Error", 'status': '400','errors':'Current Password can not be the same as old password','data':'null'},status=status.HTTP_400_BAD_REQUEST)
            else:
                user.set_password(password)
                user.save()
                return Response({'message': "Password was changed Successfully", 'status': '00', 'data':'null' },status=status.HTTP_200_OK)
        else:
            msgdetail=serializer.errors
            return Response({'message': "Invalid credentials", 'status': '00','errors':f"{msgdetail}",'data':'null'},status=status.HTTP_400_BAD_REQUEST)

