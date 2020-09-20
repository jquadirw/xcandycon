# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import pandas as pd
import datetime as dt
from django.core.validators import RegexValidator

class Accuracy(models.Model):
    since = models.DateTimeField()
    interval = models.IntegerField()
    interval_unit = models.CharField(max_length=5, blank=True, null=True)
    percent = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accuracy'

    def __repr__(self):
        return (
            "<Accuracy(since='%s', interval='%s', interval_unit='%s', percent='%s', create_date='%s')>"
            % (
                self.since,
                self.interval,
                self.interval_unit,
                self.percent,
                self.create_date,
            )
        )


class Accuracylevel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accuracylevel'

    def __repr__(self):
        return (
            "<Accuracylevel(name='%s', description='%s')>"
            % (
                self.name,
                self.description,
            )
        )

class Accuracystate(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    level = models.ForeignKey(Accuracylevel, models.DO_NOTHING, db_column='level', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accuracystate'

    def __repr__(self):
        return (
            "<Accuracystate(name='%s', description='%s', low='%s', high='%s', level='%s')>"
            % (
                self.name,
                self.description,
                self.low,
                self.high,
                self.level,
            )
        )

class Activitylog(models.Model):
    since = models.DateTimeField()
    hour = models.TimeField()
    type = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Datasource(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'datasource'

class Timezone(models.Model):
    name = models.CharField(max_length=120)
    toffset = models.IntegerField()
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'timezone'


class Source(models.Model):
    type = models.ForeignKey(Datasource, models.DO_NOTHING)
    url = models.URLField(max_length=255, null=True, blank=True, 
                          validators=[RegexValidator(regex= '/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/',
                          message='Not a valid URL',)])
    secret = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=100)
    timezone = models.ForeignKey(Timezone, models.DO_NOTHING)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'source'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    dob = models.DateTimeField()
    gender = models.CharField(max_length=1)
    source = models.ForeignKey(Source, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Direction(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direction'

    def __repr__(self):
        return (
            "<Direction(name='%s', description='%s')>"
            % (
                self.name,
                self.description,
            )
        )


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Forecast(models.Model):
    since = models.DateTimeField()
    interval = models.IntegerField()
    interval_unit = models.CharField(max_length=5, blank=True, null=True)
    value = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)

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
    since = models.DateTimeField()
    value = models.IntegerField()
    num_events = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glucose'

class Livestate(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livestate'

    def __repr__(self):
        return (
            "<Livestate(name='%s', description='%s')>"
            % (
                self.name,
                self.description,
            )
        )

class Livedata(models.Model):
    since = models.DateTimeField()
    sincemillis = models.BigIntegerField()
    glucose = models.IntegerField()
    state = models.ForeignKey(Livestate, models.DO_NOTHING, db_column='state_id', blank=True, null=True)
    direction = models.ForeignKey(Direction, models.DO_NOTHING, db_column='direction_id', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livedata'

    @property
    def timediff(self):
        timediff = (round(pd.to_numeric(((dt.datetime.utcnow() - pd.to_datetime(self.since)).value/10**9/60))))
        timediffmsg =  '{:d} mins ago'.format(timediff)
        if timediff > 59 and timediff < 1440:
            timediff /= 60
            timediff = (round(timediff))
            timediffmsg =  '{:d} hours ago'.format(timediff)
        elif timediff >= 1440:
            timediff /= 1440
            timediff = (round(timediff))
            timediffmsg =  '{:d} days ago'.format(timediff)

        return timediffmsg

    def __repr__(self):
        return (
            "<Livedata(since='%s', sincemillis='%s', glucose='%s', state='%s', direction='%s', create_date='%s')>"
            % (
                self.since,
                self.sincemillis,
                self.glucose,
                self.state,
                self.direction,
                self.create_date,
            )
        )

class Recommended(models.Model):
    since = models.DateTimeField()
    rtype = models.ForeignKey(Actytype, models.DO_NOTHING, db_column='rtype', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommended'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    accept = models.BooleanField(default=False)
    signup_confirmation = models.BooleanField(default=False)
    source = models.ForeignKey(Source, db_column='source_id', on_delete=models.CASCADE)
    livedata = models.ManyToManyField(
        Livedata,
        related_name='profiles'
    )

    def __str__(self):
        return self.user.username

    def has_source(self):
        if self.source is not None:
            return True
        else:
            return False

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
