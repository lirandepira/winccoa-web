from django import template
register = template.Library()
from datetime import datetime

@register.filter('timestamp_to_epoch')
def convert_timestamp_to_epoch(timestamp):
    # return datetime.date.fromtimestamp(int(timestamp))
    return int(timestamp.timestamp())