from rest_framework import serializers, status
from api.models import *


class ElementsSerializer(serializers.ModelSerializer):
    # element_number = serializers.RelatedField(source='element_id', read_only=True)
    class Meta:
        model = Elements
        fields = ('element_id', 'element_name')

class EventHistorySerializer(serializers.ModelSerializer):

    # element = ElementsSerializer(required=True)

    class Meta:
        model = EventHistory
        fields = ('element_id', 'ts', 'value_number')

        # fields = {
        #     'element_id': ['exact', ],
        #     'first_name': ['icontains', ],
        #     'value_number': ['exact', ],
        #     'date_joined': ['year', 'year__gt', 'year__lt', ],
        # }

    # def create(self, validated_data):
    #     element_data = validated_data.pop('element')
    #     element = ElementsSerializer.create(ElementsSerializer(), validated_data=element_data)
    #     event, created = EventHistory.objects.update_or_create(element=element,
    #                                                                 subject_major=validated_data.pop('subject_major'))