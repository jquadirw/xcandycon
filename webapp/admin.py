from django.contrib import admin
from .models import Livestate
from .models import Livedata
from .models import Direction

from .models import Forecaststate
from .models import Forecastlevel
from .models import Forecast

from .models import Accuracy
from .models import Accuracylevel
from .models import Accuracystate

from .models import Glucose
from .models import Recommended

from .models import Activitylog
from .models import Actytype
from .models import Actysubtype
from .models import Actychoice

admin.site.register(Livestate)
admin.site.register(Livedata)
admin.site.register(Direction)

admin.site.register(Forecaststate)
admin.site.register(Forecastlevel)
admin.site.register(Forecast)

admin.site.register(Accuracy)
admin.site.register(Accuracylevel)
admin.site.register(Accuracystate)

admin.site.register(Glucose)
admin.site.register(Recommended)

admin.site.register(Activitylog)
admin.site.register(Actytype)
admin.site.register(Actysubtype)
admin.site.register(Actychoice)

