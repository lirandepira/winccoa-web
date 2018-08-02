from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from api.serializer import ElementsSerializer, EventHistorySerializer
from api.api_form import ApiForm
from django.shortcuts import render
from api.models import *
from django.shortcuts import render
from .filters import EventHistoryFilter

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# JSON view which returns JSON
def json(request):

# To be used if needed to browse the Elements table

    # if request.method == 'GET':
    #     api = Elements.objects.filter(element_name__contains='Lumi')
    #     print('Before the query')
    #     tst = EventHistory.objects.filter(element_id__element_name='ECS:LHCbEfficiency.LumiTotal')
    #     print('query: '+str(tst.query))
    #     tst = EventHistory.objects.filter(element_id=2794832531230)
    #     print("Here", tst[0])
    #     serializer = ElementsSerializer(api, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    #
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = ElementsSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

# To be used if needed to browse the EventHistory table

    if request.method == 'GET':
        form = ApiForm(request.GET)
        if not form.is_valid():
            rtn = dict(
                errors=list(form.errors)
            )
            json_dump = json.dumps(rtn)
            return HttpResponseBadRequest(json_dump, content_type='text/plain')
        print(form.cleaned_data['element_name'], form.cleaned_data['starttime'])
        data = EventHistory.objects.filter(element_id__element_name=form.cleaned_data['element_name'])
        if form.cleaned_data['starttime'] is not None:
            data = data.filter(ts__gte=form.cleaned_data['starttime'])
        if form.cleaned_data['endtime'] is not None:
            data = data.filter(ts__lt=form.cleaned_data['endtime'])

        serializer = EventHistorySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Table view which returns a table with the queried elements
def search(request):
    form = ApiForm(request.GET)
    if not form.is_valid():
        rtn = dict(
            errors=list(form.errors)
        )
        json_dump = json.dumps(rtn)
        return HttpResponseBadRequest(json_dump, content_type='text/plain')
    print(form.cleaned_data['element_name'], form.cleaned_data['starttime'])
    data = EventHistory.objects.filter(element_id__element_name=form.cleaned_data['element_name'])
    if form.cleaned_data['starttime'] is not None:
        data = data.filter(ts__gte=form.cleaned_data['starttime'])
    if form.cleaned_data['endtime'] is not None:
        data = data.filter(ts__lt=form.cleaned_data['endtime'])

    return render(request, 'results.html', {'filtered_data': data, 'element_name': form.cleaned_data['element_name']})

# Plot view which returns a graph with how values change over time (Plus a table of data below).
def plot(request):
    form = ApiForm(request.GET)
    if not form.is_valid():
        rtn = dict(
            errors=list(form.errors)
        )
        json_dump = json.dumps(rtn)
        return HttpResponseBadRequest(json_dump, content_type='text/plain')
    print(form.cleaned_data['element_name'], form.cleaned_data['starttime'])
    data = EventHistory.objects.filter(element_id__element_name=form.cleaned_data['element_name'])
    if form.cleaned_data['starttime'] is not None:
        data = data.filter(ts__gte=form.cleaned_data['starttime'])
    if form.cleaned_data['endtime'] is not None:
        data = data.filter(ts__lt=form.cleaned_data['endtime'])

    return render(request, 'plot.html', {'filtered_data': data, 'element_name': form.cleaned_data['element_name']})


def _api_response(request, result):
    """
    Creates the response object for the api_* views serializing the result as a
    JSON object.

    If the argument 'callback' is included in the request, the response uses the
    JSONP pattern and the argument value is used as the callback function.
    """
    callback = request.GET.get("callback")

    res = HttpResponse(mimetype='application/json')

    if callback:
        res.write("%s(" % callback)
        json.dump(result, res)
        res.write(")")
    else:
        json.dump(result, res)

    return res
