from helmet.logger import logging
from helmet.exception import HelmetException
import sys

logging.info("Welcome to the project!")

try:
    a = 3 + '4'
    print(a)
    
except Exception as e:
    raise HelmetException(e, sys)