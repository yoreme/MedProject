from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings
import uuid
from  basemodel.models  import BaseAbstractModel
from .managers import UserManager
from datetime import datetime,timedelta
import jwt

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin,BaseAbstractModel):
    """Custom user model that support using email address instead of username """
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.EmailField(max_length=255,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    phone_no=models.CharField(max_length=15,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    is_superuser=models.BooleanField(default=False)
    # When a user no longer wishes to use our platform, they may try to delete
    is_staff=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','phone_no']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.username

    def __str__(self):
        """Return a string representation of our user"""
        return "{}".format(self.email)


    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)
        tokendata={'id':str(self.pk),'exp': int(dt.timestamp())}

        token = jwt.encode(tokendata,settings.JWT_SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class UserLoginLogoutActivity(BaseAbstractModel):
    # Login Status
    SUCCESS = 'Success'
    FAILED = 'Failed'
    LOGOUT = 'Logout'
    LOGIN = 'Login'

    STATUS = ((SUCCESS, 'Success'),
                           (FAILED, 'Failed'))
    CATEGORY = ((LOGIN, 'Login'),
                           (LOGOUT, 'Logout'))

    
    username = models.CharField(max_length=40, null=True, blank=True)
    location_IP = models.GenericIPAddressField(null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default=SUCCESS, choices=STATUS, null=True, blank=True)
    category = models.CharField(max_length=10, default=LOGIN, choices=CATEGORY, null=True, blank=True)

    class Meta:
        verbose_name = 'user_login_logout_activity'
        verbose_name_plural = 'user_login_logout_activities'
        

    def __str__(self):
        return self.category + self.status 



class UserProfile(BaseAbstractModel):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE) 
    available_online = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.user)
