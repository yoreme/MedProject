from django.contrib.auth.models import BaseUserManager
import random
import string

class UserManager(BaseUserManager):
    """Manager for User Profile """
    def create_user(self,email,phone_no,password=None,**extra_fields):
        """ Create  a new user  """
        username=extra_fields['username']
        if not email or email is None:
            raise ValueError('user must have an email address')

        if not username or username is None:
            raise ValueError('user must have a username')

        if not phone_no or  phone_no is None:
            raise ValueError("User must have an Phone number")

        if not password or password is None:
            raise ValueError("Users must have a password")

        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.username=username
        user.phone_no=phone_no
        #user.is_active=True
        #user.is_staff=False
        #user.is_superuser=False

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,phone_no,password,**extra_fields):
        """ Create and save a new superuser with given details """
        user=self.create_user(email,phone_no,password,**extra_fields)

        user.is_staff=True
        user.is_superuser=True
        user.is_verified=True

        user.save(using=self._db)
        return user

