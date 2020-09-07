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
    path('index/', views.ndx, name='ndx'),
    path('', include('social_django.urls')),
    path('home/', views.home, name="home"),
    path('addl_info/', views.addl_info, name="addl_info"),
    path("login/", views.login, name="login"),
    path('profile/', views.profile),
    path("register/", views.register, name="register"),
    path("sent/", views.activation_sent_view, name="activation_sent"),
    path("activate/<slug:uidb64>/<slug:token>/", views.activate, name="activate"),
    path('logout/', views.logout, name="logout"),
    path('visualize/', views.visualize),
    path('recipe/', views.recipe),
    path('learn/', views.learn),
    path('help/', views.help),
    path('settings/', views.settings),
]
