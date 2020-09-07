import csv
import pandas as pd
import logging
from django.core.validators import URLValidator

from django.core.cache import cache

logger = logging.getLogger(__name__)

def is_valid(url):
     url = URLValidator()
     valid = False
     try:
          url(a)
          valid = True
     except:
          valid = False

     return valid

