from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

from django.views.generic.base import View
from bootstrap_modal_forms.generic import (BSModalReadView)

from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy

import logging
import pandas as pd
import seaborn as sns
import urllib, base64
import io

from .models import Livedata
from .models import Forecast
from .models import Accuracy
from .models import Glucose
from .models import Recommended
from .models import Activitylog

from django.core.cache import cache

logger = logging.getLogger(__name__)

def index(request):
    functions = Function.objects.all()

    context = {
        'functions': functions,
    }

    return render(request, 'webapp/index.html', context)

@login_required
def home(request):
    try:
        livedata = Livedata.objects.latest('id')
    except Livedata.DoesNotExist:
        livedata = None

    try:
        forecasts = Forecast.objects.all().order_by('-id')[:2][::-1]
    except Forecast.DoesNotExist:
        forecasts = None

    try:
        accuracies = Accuracy.objects.all().order_by('-id')[:2][::-1]
    except Accuracy.DoesNotExist:
        accuracies = None

    try:
        recommended = Recommended.objects.latest('id')
    except Recommended.DoesNotExist:
        recommended = None

    try:
        glucose = Glucose.objects.latest('id')
    except Glucose.DoesNotExist:
        glucose = None

    try:
        activitylog = Activitylog.objects.latest('id')
    except Activitylog.DoesNotExist:
        activitylog = None

    context = {
                'livedata': livedata, 
                'forecasts': forecasts, 
                'accuracies': accuracies, 
                'glucose': glucose, 
                'activitylog': activitylog, 
                'recommended': recommended
               }
    return render(request, 'webapp/home.html', context)

@login_required
def profile(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'webapp/profile.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

@login_required
def data(request):
    return render(request, 'webapp/dq/home.html')

@login_required
def visualize(request):
    return render(request, 'webapp/da/visualize.html')

@login_required
def learn(request):
    return render(request, 'webapp/dl/learn.html')

@login_required
def recipe(request):
    return render(request, 'webapp/re/recipe.html')

def help(request):
    return render(request, 'webapp/co/help.html')

def settings(request):
    return render(request, 'webapp/co/settings.html')

@login_required
def analytics(request):
    return render(request, 'webapp/da/home.html')

def logout(request):
    django_logout(request)
    domain = 'dev-utjtfsx4.auth0.com'
    client_id = '8SY0HohBHyj0vMT0yHJ2j7gmjzACbL62'
    return_to = 'http://localhost:8000'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

# Error Pages
def not_found(request, exception, template_name="404.html"):
    response = render("webapp/errors/404.html")
    response.status_code = 404
    return response

def server_error(request):
    context = {
        'code': '500',
        'message': 'Oops! unexpected error encountered.'
    }

    return render(request, 'webapp/errors/500.html', context)

def permission_denied(request, exception, template_name="403.html"):
    response = render("webapp/errors/403.html")
    response.status_code = 403
    return response

def bad_request(request, exception, template_name="400.html"):
    response = render("webapp/errors/400.html")
    response.status_code = 400
    return response
