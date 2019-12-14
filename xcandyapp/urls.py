"""xcandyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from webapp import views

urlpatterns = [
    path('', include('webapp.urls')),
    path('admin/', admin.site.urls),
]

# Other URL confs up here

# Do not import anything for the handler404,
# or whatnot from the django.conf.urls
# Just list them below

handler404 = 'webapp.views.not_found'
handler500 = 'webapp.views.server_error'
handler403 = 'webapp.views.permission_denied'
handler400 = 'webapp.views.bad_request'
