import pandas as pd
import logging
from django.core.validators import URLValidator
from django.core.cache import cache
from datetime import datetime, timedelta

from .models import Glucose

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

def glucose(profile, profilelivedata, period):
     try:
          numEvents = 0
          prevId = 0

          glucose_low_limit = profile.prefs.glucose_low_limit
          if glucose_low_limit is None or 0:
               glucose_low_limit = 80

          glucose_high_limit = profile.prefs.glucose_high_limit
          if glucose_high_limit is None or 0:
               glucose_high_limit = 140

          time_period_hours_ago = datetime.utcnow() - timedelta(days=period)
          gdata = profilelivedata.filter(since__gte=time_period_hours_ago).aggregate(Avg('glucose'))
          hypos = profilelivedata.filter(since__gte=time_period_hours_ago).filter(glucose__lt=glucose_low_limit).all()

          for hypo in hypos:
               if hypo.id != prevId + 1:
                    numEvents += 1
               prevId = hypo.id

          glucose = Glucose(since=24, value=gdata['glucose__avg'], num_events=numEvents)
     except Glucose.DoesNotExist:
          glucose = None

     return glucose

