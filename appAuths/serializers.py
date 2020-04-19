from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
import re

from .models import User,UserProfile
import utils.service  as services

import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
    )
logger = logging.getLogger(__name__)


class RegistrationSerializer(serializers.Serializer):
    """Serializers registration requests and creates a new user."""
    email = serializers.EmailField(max_length=128,
                                     write_only=True,
                                     required=True,)
    username = serializers.CharField(max_length=128,
                                     write_only=True,
                                     required=True,)
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        style={'input_type': 'password'},
        max_length=128,
        min_length=8,
        write_only=True
    )
    first_name = serializers.CharField(max_length=255, write_only=True)
    last_name = serializers.CharField(max_length=255, write_only=True)
    phone_no = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email','username','phone_no', 'password','first_name','last_name']

    def validate(self, attrs):
        email = attrs.get('email',None)
        username = attrs.get('username',None)
        password = attrs.get('password',None)
        phone_no = attrs.get('phone_no',None)
      
        password_pattern = services.PASSWORD_PATTERN
        email_pattern = services.EMAIL_PATTERN
        phone_pattern = services.PHONE_PATTERN
        phone_pattern_rule = services.number_rule
        logger.info('phone_pattern_rule:{}'.format(phone_pattern_rule))


        #USERNAME VALIDATION
        if username is None:
            raise serializers.ValidationError(
                'username is required to log in.'
            )

        if User.objects.filter(username=username).exists():
            return serializers.ValidationError('This username: {} , already belongs to a user on lottoly'.format(username))
        else:
            logger.info('user username looks good')

        
        #EMAIL VALIDATION
        #check with email pattern
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if re.match(email_pattern,email):
            #user = [i for i in User.objects.all() if i.email.upper() == email.upper()]
            #if user:
            if User.objects.filter(email=email).exists():
                return serializers.ValidationError('This email: {} , already belongs to a user on lottoly'.format(email))
            else:
                logger.info('user email looks good')
        else:
            return serializers.ValidationError('Email: {} is not valid'.format(email))

        #check if email exist in user table

        #PASSWORD VALIDATION 
        #validating password

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        #check password pattern  
        if not re.match(password_pattern,password):
            return serializers.ValidationError('Password is weak, please use atleast 1 UPPERCASE, 1 LOWERCASE, 1 SYMBOL')

        #PHONE NUMBER VALIDATION
        #validating phone
        if phone_no is None:
            raise serializers.ValidationError(
                'A phone number is required to log in.'
            )
         
        if re.match(phone_pattern,phone_no) or (phone_no.startswith('0') and len(phone_no)==11):
            if phone_pattern_rule(phone_no):
                #userx = [i for i in  User.objects.all() if i.phone_no[-10:] == phone_no[-10:]]
                #if not userx:
                if User.objects.filter(phone_no__exact=phone_no).exists():
                    return serializers.ValidationError('This phone number: {} , already belongs to a user on spread messaging'.format(phone_no))
        else:

            return serializers.ValidationError('This phone number: {} is not valid'.format(phone_no))
        
        return attrs
        
    def create(self, validated_data):
        logger.info('Create method called with data {}'.format(validated_data))
        # Use the `create_user` method we wrote earlier to create a new user.
        user=User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)
        return user




class LoginSerializer(serializers.Serializer):
    """ Serializer Login requests for registered user. """
    email = serializers.CharField(max_length=128,
                                     write_only=True,
                                     required=True,)
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={'input_type': 'password'},
                                    trim_whitespace=False)

    #We are to ignore this field on login is jus to display the value after login
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        email = attrs.get('email',None)
        password = attrs.get('password',None)

        email_pattern = services.EMAIL_PATTERN
        if email is None:
                raise serializers.ValidationError(
                    'An email address or username is required to log in.'
                )

        if '@' in email:
            if not re.match(email_pattern,email):
                return serializers.ValidationError('Email: {} is not valid'.format(email))
        
        if password is None:
                raise serializers.ValidationError(
                    'A password is required to log in.'
                )

        return attrs




class LogoutSerializer(serializers.ModelSerializer):
    """ Serializer Login requests for registered user. """
    email = serializers.EmailField(max_length=128,
                                     write_only=True,
                                     required=True,)
    token = serializers.CharField(max_length=255, read_only=True)




class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={'input_type': 'password'},required=True)
    new_password = serializers.CharField(style={'input_type': 'password'},required=True)

    def validate(self, attrs):
        new_password = attrs.get('new_password',None)
        current_password = attrs.get('current_password',None)
        password_pattern = services.PASSWORD_PATTERN

        if new_password is None:
            raise serializers.ValidationError('A password is required.')
            
        if not re.match(password_pattern,new_password):
            return serializers.ValidationError('Password is weak, please use atleast 1 UPPERCASE, 1 LOWERCASE, 1 SYMBOL')

        if current_password is None:
            raise serializers.ValidationError('Current password is required.')

        if not re.match(password_pattern,current_password):
            return serializers.ValidationError('Current Password is weak, please use atleast 1 UPPERCASE, 1 LOWERCASE, 1 SYMBOL')
        
        if not new_password==current_password:
            return serializers.ValidationError('Current and Confirm Password must be equal')

        return attrs

     

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255,write_only=True,required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'},max_length=128,write_only=True,required=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'},max_length=128,write_only=True,required=True)
    email = serializers.CharField(max_length=255,write_only=True,required=True)


    def validate(self, attrs):
        token = attrs.get('token',None)
        new_password = attrs.get('password',None)
        current_password = attrs.get('confirm_password',None)
        password_pattern = services.PASSWORD_PATTERN

        if token is None:
            raise serializers.ValidationError('Token is required.')

        if new_password is None:
            raise serializers.ValidationError('A password is required.')
            
        if not re.match(password_pattern,new_password):
            return serializers.ValidationError('Password is weak, please use atleast 1 UPPERCASE, 1 LOWERCASE, 1 SYMBOL')

        if current_password is None:
            raise serializers.ValidationError('Confirm password is required.')

        if not re.match(password_pattern,current_password):
            return serializers.ValidationError('Current Password is weak, please use atleast 1 UPPERCASE, 1 LOWERCASE, 1 SYMBOL')
        
        if not new_password==current_password:
            return serializers.ValidationError('Current and Confirm Password must be equal')

        return attrs


class UserSerializer(serializers.ModelSerializer):
    """ Serializer user profile object """
    class Meta:
        model=User
        fields=('id','email','username','phone_no','password','first_name','last_name')
        read_only_fields = ('id',)
        extra_kwargs={
            'id': {
                'read_only': True
            },
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    
