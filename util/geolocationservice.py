from django.conf import settings
from ipdata import ipdata
from pprint import pprint
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
"""
To get user geo location service using ipaddress
"""

class geolocationClient:  
    API_KEY = '1fedcb73d9a45ffb9e0652bf68bef7ace46f8394b6d944c3351941bf'
    @classmethod
    def get_location(cls,ip_address):
        logger.info('start:getting user location service using ipaddress')
        try:
            if ip_address is not None:
                ipdata = ipdata.IPData(self.API_KEY)
                response = ipdata.lookup(ip_address)
                logger.info('ipdata response response: {},response code :{}'.format(response.json(),response.status_code))
                return response.json()
               
        except Exception as e:
            logger.error('there was an error sending email, info : {} '.format(e))
            return None