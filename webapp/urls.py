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
    path('mydiet/', views.mydiet),
    path('learn/', views.learn),
    path('help/', views.help),
    path('da/import', views.importframe, name='import'),
    path('da/view/<str:source>/<str:view>', views.fview, name='frame_view'),
    path('da/corr/<str:source>/<str:view>', views.correlationform, name='correlation_form'),
    path('da/heat/<str:source>/<str:view>', views.heatmapform, name='heatmap_form'),
    path('da/enrich', views.enrich, name='enrich'),
    path('da/filter', views.filter, name='filter'),
    path('da/merge', views.merge, name='merge'),
    path('da/slice', views.slice, name='slice'),
    path('ml/', views.mlearn, name='ml_home'),
    path('ml/init', views.init_ml, name='init_ml'),
]
