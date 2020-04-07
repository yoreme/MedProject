from django.conf import settings
from ipdata import ipdata
import requests
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
"""
To get user geo location service using ipaddress
"""

class geolocationClient:  
    API_KEY = '1fedcb73d9a45ffb9e0652bf68bef7ace46f8394b6d944c3351941bf'
    BASE_URL='https://api.ipdata.co/{}?api-key={}'
    @classmethod
    def get_location(cls,ip_address):
        logger.info('start:getting user location service using ipaddress:{}'.format(ip_address))
        try:
            if ip_address is not None:
                #ipdata = ipdata.IPData(cls.API_KEY)
                response = requests.get('https://api.ipdata.co/{}?api-key={}'.format('188.148.194.57',cls.API_KEY))
                #ipdata.lookup(ip_address)
                print(response)
                logger.info('ipdata response response data: {}'.format(response.json()))
                return response.json()
               
        except Exception as e:
            logger.error('there was an error sending email, info : {} '.format(e))
            return None