from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from djoser.signals import user_activated,user_registered
from django.dispatch import receiver
from django.conf import settings
from django.db.models import Q
from django.core.signals import request_finished
from django.contrib.auth.tokens import default_token_generator

#from utils.monnifyservice import ExtendedRequests,ExtendedRequests2,MONNIFY_URLS

from .models import UserLoginLogoutActivity,UserProfile
import logging


logger= logging.getLogger(__name__)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginLogoutActivity(location_IP=get_client_ip(request),
                                                    username=user.email,
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginLogoutActivity.SUCCESS,
                                                    category=UserLoginLogoutActivity.LOGIN)
        user_login_activity_log.save()
    except Exception as e:
        # log the error
        logger.error("log_user_logged_in request: %s, error: %s" % (request, e))



@receiver(user_login_failed)
def log_user_logged_in_failed(sender, credentials, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log = UserLoginLogoutActivity(locatiom_IP=get_client_ip(request),
                                                    username=credentials['email'],
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginLogoutActivity.FAILED,
                                                    category=UserLoginLogoutActivity.LOGIN)
        user_login_activity_log.save()
    except Exception as e:
        # log the error
        logger.error("log_user_logged_in request: %s, error: %s" % (request, e))



@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_logout_activity_log = UserLoginLogoutActivity(location_IP=get_client_ip(request),
                                                    username=user.email,
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginLogoutActivity.SUCCESS,
                                                    category=UserLoginLogoutActivity.LOGOUT)
        user_logout_activity_log.save()
    except Exception as e:
        # log the error
        logger.error("log_user_logged_in request: %s, error: %s" % (request, e))

