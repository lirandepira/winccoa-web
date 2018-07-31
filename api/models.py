from django.db import models

class Elements(models.Model):
    element_id = models.IntegerField(primary_key=True)
    event = models.IntegerField()
    alert = models.IntegerField()
    element_name = models.CharField(max_length=400)
    unit = models.CharField(max_length=400)
    alias = models.CharField(max_length=400)
    group_name = models.CharField(max_length=400)
    comment = models.CharField(max_length=400, db_column='comment_')
    _type = models.IntegerField(db_column='type_')

    class Meta:
        managed = False
        app_label = 'winccoa'
        db_table = 'S362_LB_ELEMENTS'

class EventHistory(models.Model):
    element_id = models.ForeignKey(Elements, on_delete=models.CASCADE, db_column='element_id', primary_key=True, related_name='element_no')
    ts = models.DateTimeField(primary_key=True)
    value_number = models.FloatField()
    status = models.IntegerField(blank=True, null=True)
    manager = models.IntegerField()
    user = models.IntegerField(db_column='user_')
    base = models.IntegerField()
    text = models.CharField(max_length=400)
    value_string = models.CharField(max_length=400)
    value_timestamp = models.DateTimeField()
    corrvalue_number = models.FloatField()
    olvalue_number = models.FloatField()
    corrvalue_string = models.CharField(max_length=400)
    olvalue_string = models.CharField(max_length=400)
    corrvalue_timestamp = models.DateTimeField()
    olvalue_timestamp = models.DateTimeField()

    class Meta:
        managed = False
        app_label = 'winccoa'
        db_table = 'S362_LB_EVENTHISTORY'
