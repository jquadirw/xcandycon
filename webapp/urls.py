from django.urls import path
from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from . import views

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')),
    path('home/', views.home),
    path('profile/', views.profile),
    path('logout/', views.logout),
    path('visualize/', views.visualize),
    path('recipe/', views.recipe),
    path('learn/', views.learn),
    path('help/', views.help),
    path('settings/', views.settings),
]
