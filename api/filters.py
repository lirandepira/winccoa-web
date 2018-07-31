import django_filters
from api.models import *

class EventHistoryFilter(django_filters.FilterSet):
    class Meta:
        model = EventHistory
        fields = ['element_id', 'ts', 'value_number', ]