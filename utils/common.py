from django.conf import settings
from django.template.loader import render_to_string
from dateutil.parser import parse
from datetime import datetime, date

EMAIL_PATTERN = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
PASSWORD_PATTERN = "\A(?=[a-z,A-Z,0-9,\s]*[^a-z,A-Z,0-9,\s])(?=\D*\d).{8,100}" 

def get_client_ip(request):
    """
    Return the ip address of a request .

    :param request: str, request
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def valid_date(datestring):
    """
    Return whether the string can be interpreted as a date format.
    """
    try:
        datetime.strptime(datestring, '%d-%m-%Y')
        return True
    except ValueError:
        return False
