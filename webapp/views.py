from django.shortcuts import render
from django.shortcuts import render_to_response
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

from .models import Product
from .models import Function
from .forms import FrameForm
from .forms import ExpImportForm
from .forms import CorrelationForm
from .forms import HeatmapForm
from .models import Frame

from .functions import process_frame

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
    return render(request, 'webapp/home.html')

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

def importframe(request):
    if request.method == 'POST':
        frameform = FrameForm(request.POST, request.FILES)
        if frameform.is_valid():
            files = request.FILES.getlist('filefield')
            for f in files:
                if f in cache:
                    frame = cache.get(f)
                else:
                    frame = process_frame(f)

            context = {
                'frame': frame,
            }

        return render(request, 'webapp/da/frame.html', context)
    else:
        frame = FrameForm()
        context = {
            'form': frame
        }

        return render(request,"webapp/da/import.html", context)

@login_required
def data(request):
    return render(request, 'webapp/dq/home.html')

@login_required
def enrich(request):
    if request.method == 'POST':
        template_name = 'webapp/dq/enrich.html'
    else:
        template_name = 'webapp/dq/enrich.html'

    jsonresponse = save_correlation_form(request, form, frame, view, template_name)
    return jsonresponse

@login_required
def filter(request):
    if request.method == 'POST':
        template_name = 'webapp/dq/filter.html'
    else:
        template_name = 'webapp/dq/filter.html'

    jsonresponse = save_correlation_form(request, form, frame, view, template_name)
    return jsonresponse

@login_required
def merge(request):
    if request.method == 'POST':
        template_name = 'webapp/dq/merge.html'
    else:
        template_name = 'webapp/dq/merge.html'

    jsonresponse = save_correlation_form(request, form, frame, view, template_name)
    return jsonresponse

@login_required
def slice(request):
    if request.method == 'POST':
        template_name = 'webapp/dq/slice.html'
    else:
        template_name = 'webapp/dq/slice.html'

    jsonresponse = save_correlation_form(request, form, frame, view, template_name)
    return jsonresponse

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

@login_required
def fview(request, source, view):
    frame = cache.get(source)
    data = dict()
    data['html_title'] = view

    if 'Quick' in view:
        data['html_form'] = frame.data
    elif 'Statistics' in view:
        data['html_form'] = frame.stats
    else:
        data['html_form'] = frame.stats

    return JsonResponse(data)

@login_required
def correlationform(request, source, view):
    frame = cache.get(source)

    if request.method == 'POST':
        xcolumns = request.POST.getlist('xcolumns')
        ycolumns = request.POST.getlist('ycolumns')

        form = CorrelationForm(request.POST, initial={'id': source}, xcolumns=xcolumns, ycolumns=ycolumns)
        template_name = 'webapp/da/includes/partial_correlation_results.html'
    else:
        form = CorrelationForm(initial={'id': source}, xcolumns=frame.columns, ycolumns=frame.columns)
        template_name = 'webapp/da/includes/partial_correlation.html'

    jsonresponse = save_correlation_form(request, form, frame, view, template_name)
    return jsonresponse

@login_required
def heatmapform(request, source, view):
    frame = cache.get(source)

    if request.method == 'POST':
        pivotCols = request.POST.getlist('pivotCols')
        valueCols = request.POST.getlist('valueCol')
        indexCols = request.POST.getlist('indexCol')
        columnCols = request.POST.getlist('columnCols')
        cma = request.POST.getlist('cma')

        form = HeatmapForm(request.POST, initial={'id': source}, pivotCols=pivotCols, valueCols=valueCols, indexCols=indexCols, columnCols=columnCols, cma=cma)
        template_name = 'webapp/da/includes/partial_heatmap_results.html'
    else:
        cma_choices = ('BuGn_r', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                       'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
                       'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar')
        form = HeatmapForm(initial={'id': source}, pivotCols=frame.columns, valueCols=frame.columns, indexCols=frame.columns, columnCols=frame.columns, cma=cma_choices)
        template_name = 'webapp/da/includes/partial_heatmap.html'

    jsonresponse = save_heatmap_form(request, form, frame, view, template_name)
    return jsonresponse

def getCorrelation(frame, xcolumns, ycolumns):
    fig = sns.pairplot(frame.alldata, x_vars=xcolumns, y_vars=ycolumns)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def getHeatmap(frame, pivotCols, valueCols, indexCols, columnCols, cma):
    heatmap_df = frame.alldata[pivotCols]
    heatmap1_data = heatmap_df.pivot_table(index=indexCols,
                                           columns=columnCols,
                                           values=valueCols)

    cmapColor = cma
    print(cma)
    if (cma is None or not cma):
        cmapColor = "ocean"

    svm = sns.heatmap(heatmap1_data, cmap=cmapColor, annot=False, linewidths=0.0, cbar=True)
    fig = svm.get_figure()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', pad_inches=0.1)
    buf.seek(0)
    string = base64.b64encode(buf.read())

    heatmap = 'data:image/png;base64,' + urllib.parse.quote(string)
    return heatmap

def save_correlation_form(request, form, frame, view, template_name):
    data = dict()
    data['html_title'] = view

    context = {
        'form': form,
        'source': frame.source,
    }

    if request.method == 'POST':
        xcolumns = request.POST.getlist('xcolumns')
        ycolumns = request.POST.getlist('ycolumns')

        uri = getCorrelation(frame, xcolumns, ycolumns)

        if uri is not None:
            data['form_is_valid'] = True

            data['uri'] = uri
            context['uri'] = uri
            context['has_uri'] = True
        else:
            data['form_is_valid'] = False
            context['has_uri'] = False

    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def save_heatmap_form(request, form, frame, view, template_name):
    data = dict()
    data['html_title'] = view

    context = {
        'form': form,
        'source': frame.source,
    }

    if request.method == 'POST':
        pivotCols = request.POST.getlist('pivotCols')
        valueCols = request.POST.getlist('valueCols')
        indexCols = request.POST.getlist('indexCols')
        columnCols = request.POST.getlist('columnCols')
        cma = request.POST.get('cma')

        heatmap = getHeatmap(frame, pivotCols, valueCols, indexCols, columnCols, cma)

        if heatmap is not None:
            data['form_is_valid'] = True

            data['heatmap'] = heatmap
            context['heatmap'] = heatmap
            context['has_heatmap'] = True
        else:
            data['form_is_valid'] = False
            context['has_heatmap'] = False

    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def mlearn(request):
    return render(request, 'webapp/ml/home.html')

@login_required
def init_ml(request):
    if request.method == 'POST':
        frameform = FrameForm(request.POST, request.FILES)
        if frameform.is_valid():
            files = request.FILES.getlist('filefield')
            for f in files:
                if f in cache:
                    frame = cache.get(f)
                else:
                    frame = process_frame(f)

            context = {
                'frame': frame,
            }

        return render(request, 'webapp/da/frame.html', context)
    else:
        form = ExpImportForm()
        context = {
            'form': form
        }

        return render(request,"webapp/ml/import.html", context)

def logout(request):
    django_logout(request)
    domain = 'dev-utjtfsx4.auth0.com'
    client_id = '8SY0HohBHyj0vMT0yHJ2j7gmjzACbL62'
    return_to = 'http://localhost:8000'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

# Error Pages
def not_found(request, exception, template_name="404.html"):
    response = render_to_response("webapp/errors/404.html")
    response.status_code = 404
    return response

def server_error(request):
    context = {
        'code': '500',
        'message': 'Oops! unexpected error encountered.'
    }

    return render(request, 'webapp/errors/500.html', context)

def permission_denied(request, exception, template_name="403.html"):
    response = render_to_response("webapp/errors/403.html")
    response.status_code = 403
    return response

def bad_request(request, exception, template_name="400.html"):
    response = render_to_response("webapp/errors/400.html")
    response.status_code = 400
    return response
