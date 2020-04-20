from django.conf import settings
from django.template.loader import render_to_string

EMAIL_PATTERN = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
PASSWORD_PATTERN = "\A(?=[a-z,A-Z,0-9,\s]*[^a-z,A-Z,0-9,\s])(?=\D*\d).{8,100}" 

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

