from django.contrib import admin
from .models import Product
from .models import Function
from .models import Correlation
from .models import ColorScheme

admin.site.register(Product)
admin.site.register(Function)
admin.site.register(Correlation)
admin.site.register(ColorScheme)
