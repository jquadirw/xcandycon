from django.contrib import admin
from .models import User
from .models import Indicator
from .models import LiveState
from .models import LiveData

from .models import ForecastState
from .models import ForecastLearned
from .models import Forecast

admin.site.register(User)
admin.site.register(Indicator)
admin.site.register(LiveState)
admin.site.register(LiveData)

admin.site.register(ForecastState)
admin.site.register(ForecastLearned)
admin.site.register(Forecast)
