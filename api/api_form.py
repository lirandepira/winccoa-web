from django import forms
import django_filters
# from django.contrib.auth.models import Elements
# from typing import List

from api.models import *


class ApiForm(forms.Form):
    """
    The form used for the query arguments of the api_search view.
    """
    rows = forms.IntegerField(min_value=-1, required=False)
    start = forms.IntegerField(min_value=0, required=False)

    starttime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S',], required=False)
    endtime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S',], required=False)

    #element_id = forms.IntegerField(required=False)
    element_name = forms.CharField(required=True)

class ElementSearch(django_filters.FilterSet):
    class Meta:
        model = EventHistory
        fields = ['element_id', 'ts', 'value_number', ]