import json
from django.contrib.auth.decorators import login_required

from django.views.generic.base import View
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse

from django.contrib.auth import login as django_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib import messages
import requests
import logging
import pandas as pd
import seaborn as sns
import urllib, base64
import io
from django import forms
from datetime import datetime, timedelta
from django.db.models import Avg, Count, Q

from .functions import *

from .models import *

from .forms import SignUpForm
from .forms import SignInForm
from .forms import AddlInfoForm

from django.core.cache import cache

logger = logging.getLogger(__name__)

def index(request):
    form = SignUpForm()
    return render(request, 'webapp/index.html', {"form": form})

def ndx(request):
    show = request.GET['s']
    if show == 'login':
        form = SignInForm()
        msg = show
    else:
        form = SignUpForm()
    return render(request, 'webapp/index.html', {"form": form, "msg": msg})

def login(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = SignInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.login(request)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # If the account is valid and active, we can log the user in.
            # We'll send the user back to the homepage.
            django_login(request, user)

            print("profile has source = ", user.profile.has_source)
            if user.profile.has_source == False:
                redirect("addl_info")

            return redirect("home")

    # No context variables to pass to the template system, hence the
    # blank dictionary object...
    return render(request, "webapp/index.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.profile.username = form.cleaned_data.get("username")
            user.profile.email = form.cleaned_data.get("email")
            user.profile.password1 = form.cleaned_data.get("password1")
            user.profile.password2 = form.cleaned_data.get("password2")
            user.profile.first_name = form.cleaned_data.get("first_name")
            user.profile.last_name = form.cleaned_data.get("last_name")
            user.profile.accept = form.cleaned_data.get("accept")
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Please Activate Your Account"
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string(
                "webapp/includes/activation_request.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            user.email_user(subject, message)
            messages.success(request, "Sign up successful. A link has been sent to your email with further instructions.")
    else:
        form = SignUpForm()
    return render(request, "webapp/index.html", {"form": form})

def addl_info(request):
    if request.method == "POST":
        sourceobj = Source()
        typeid = request.POST["source"]
        datasource = Datasource.objects.get(id=typeid)
        sourceobj.type = datasource

        sourceobj.url = request.POST["url"]
        sourceobj.url += '/api/v1/entries?count=10000&find[date][$gt]='
        sourceobj.secret = request.POST["secret"]
        sourceobj.location = request.POST["location"]
        timezoneid = request.POST["timezone"]

        timezone = Timezone.objects.get(id=timezoneid)
        sourceobj.timezone = timezone

        request.user.profile.source = sourceobj
        sourceobj.save()
        request.user.profile.save()

        return redirect("home")

    return render(request, "webapp/signup/addl_info.html")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        django_login(request, user)
        return redirect("addl_info")
    else:
        return render(request, "webapp/includes/activation_invalid.html")

def activation_sent_view(request):
    return render(request, "webapp/includes/activation_sent.html")

@login_required
def home(request):
    profile = request.user.profile
    profilelivedata = profile.livedata
    try:
        livedata = profilelivedata.latest('id')
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
        time_24_hours_ago = datetime.utcnow() - timedelta(days=1)
        gdata = profilelivedata.filter(since__gte=time_24_hours_ago).aggregate(Avg('glucose'))
        numEvents = 0
        prevId = 0
        # hypos = profilelivedata.filter(since__gte=time_24_hours_ago).filter(glucose__lt=100).aggregate(Count('id'))
        hypos = profilelivedata.filter(since__gte=time_24_hours_ago).filter(glucose__lt=100).all()
        for hypo in hypos:
            if hypo.id != prevId:
                numEvents += 1
            prevId = hypo.id

        print("########## avg glucose = ", gdata['glucose__avg'], ", numEvents = ", numEvents)
        # glucose = Glucose(since=24, value=gdata['glucose__avg'], num_events=hypos['id__count'])
        glucose = Glucose(since=24, value=gdata['glucose__avg'], num_events=numEvents)
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
    return redirect("index")

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
