from django.conf import settings
from django.template.loader import render_to_string

EMAIL_PATTERN = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
PHONE_PATTERN = '\A(?=(\+?234[^0]+)).{10,16}'
PASSWORD_PATTERN = "\A(?=[a-z,A-Z,0-9,\s]*[^a-z,A-Z,0-9,\s])(?=\D*\d).{8,100}" 
