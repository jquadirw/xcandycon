# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accuracy(models.Model):
    since = models.DateField()
    interval = models.IntegerField()
    interval_unit = models.CharField(max_length=5, blank=True, null=True)
    percent = models.IntegerField()
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accuracy'


class Accuracylevel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accuracylevel'


class Accuracystate(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    level = models.ForeignKey(Accuracylevel, models.DO_NOTHING, db_column='level', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accuracystate'


class Activitylog(models.Model):
    since = models.DateField()
    hour = models.TimeField()
    type = models.IntegerField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activitylog'


class Actychoice(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actychoice'


class Actysubtype(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actysubtype'


class Actytype(models.Model):
    name = models.CharField(max_length=20)
    subtype = models.ForeignKey(Actysubtype, models.DO_NOTHING, db_column='subtype', blank=True, null=True)
    choice = models.ForeignKey(Actychoice, models.DO_NOTHING, db_column='choice', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actytype'


class Direction(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direction'


class Forecast(models.Model):
    since = models.DateField()
    interval = models.IntegerField()
    interval_unit = models.CharField(max_length=5, blank=True, null=True)
    value = models.IntegerField()
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forecast'


class Forecastlevel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forecastlevel'


class Forecaststate(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    level = models.ForeignKey(Forecastlevel, models.DO_NOTHING, db_column='level', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forecaststate'


class Glucose(models.Model):
    since = models.DateField()
    value = models.IntegerField()
    num_events = models.IntegerField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glucose'


class Livedata(models.Model):
    since = models.DateField()
    glucose = models.IntegerField()
    state = models.ForeignKey('Livestate', models.DO_NOTHING, db_column='state', blank=True, null=True)
    direction = models.ForeignKey(Direction, models.DO_NOTHING, db_column='direction', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livedata'


class Livestate(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livestate'


class Recommended(models.Model):
    since = models.DateField()
    rtype = models.ForeignKey(Actytype, models.DO_NOTHING, db_column='rtype', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommended'
