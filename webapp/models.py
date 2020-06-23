# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    device = models.CharField(max_length=30, blank=True, null=True)
    serial_num = models.CharField(max_length=40, blank=True, null=True)
    datetime = models.CharField(max_length=40)
    record_type = models.CharField(max_length=5, blank=True, null=True)
    glucose = models.IntegerField(blank=True, null=True)
    glucose_unit = models.CharField(max_length=10, blank=True, null=True)
    scang = models.IntegerField(blank=True, null=True)
    scang_unit = models.CharField(max_length=10, blank=True, null=True)
    rai = models.IntegerField(blank=True, null=True)
    rai_unit = models.CharField(max_length=10, blank=True, null=True)
    food = models.CharField(max_length=20, blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)
    carbs_unit = models.CharField(max_length=10, blank=True, null=True)
    lai = models.IntegerField(blank=True, null=True)
    lai_unit = models.CharField(max_length=10, blank=True, null=True)
    stripg = models.IntegerField(blank=True, null=True)
    stripg_unit = models.CharField(max_length=10, blank=True, null=True)
    ketone = models.IntegerField(blank=True, null=True)
    ketone_unit = models.CharField(max_length=10, blank=True, null=True)
    mi = models.IntegerField(blank=True, null=True)
    mi_unit = models.CharField(max_length=10, blank=True, null=True)
    ci = models.IntegerField(blank=True, null=True)
    ci_unit = models.CharField(max_length=10, blank=True, null=True)
    uci = models.IntegerField(blank=True, null=True)
    uci_unit = models.CharField(max_length=10, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey('ActivityState', models.DO_NOTHING, db_column='state', blank=True, null=True)
    when = models.DateTimeField()
    who = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class Activity2ActivityLogDetail(models.Model):
    activity_log = models.ForeignKey('ActivityLog', models.DO_NOTHING)
    activity_log_detail = models.ForeignKey('ActivityLogDetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'activity_2_activity_log_detail'


class ActivityAction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_action'


class ActivityHow(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_how'


class ActivityLog(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'activity_log'


class ActivityLogDetail(models.Model):
    time = models.TimeField()
    value = models.IntegerField()
    radius = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('ActivityType', models.DO_NOTHING, db_column='type')
    state = models.ForeignKey('ActivityState', models.DO_NOTHING, db_column='state')

    class Meta:
        managed = False
        db_table = 'activity_log_detail'


class ActivityRecommended(models.Model):
    since = models.DateTimeField()
    when = models.DateTimeField()
    type = models.ForeignKey('ActivityType', models.DO_NOTHING, db_column='type')
    action = models.ForeignKey(ActivityAction, models.DO_NOTHING, db_column='action', blank=True, null=True)
    how = models.ForeignKey(ActivityHow, models.DO_NOTHING, db_column='how')

    class Meta:
        managed = False
        db_table = 'activity_recommended'


class ActivityState(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_state'


class ActivityType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_type'


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

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


class BatchHistory(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    filename = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    when = models.DateTimeField()
    who = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_history'


class BatchState(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_state'


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Forecast(models.Model):
    since = models.DateTimeField()
    when = models.DateTimeField()
    interval = models.IntegerField(blank=True, null=True)
    interval_unit = models.CharField(max_length=10, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forecast'


class ForecastLearned(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    level = models.ForeignKey('Level', models.DO_NOTHING, db_column='level')

    class Meta:
        managed = False
        db_table = 'forecast_learned'


class ForecastState(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)
    low = models.IntegerField()
    high = models.IntegerField()
    level = models.ForeignKey('Level', models.DO_NOTHING, db_column='level')

    class Meta:
        managed = False
        db_table = 'forecast_state'


class Glucose(models.Model):
    since = models.DateTimeField()
    when = models.DateTimeField()
    value = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, db_column='event', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glucose'


class GlucoseMode(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glucose_mode'


class Indicator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator'


class Level(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level'


class LiveData(models.Model):
    since = models.DateTimeField()
    when = models.DateTimeField()
    glucose = models.IntegerField(blank=True, null=True)
    glucose_unit = models.CharField(max_length=10, blank=True, null=True)
    glucose_indicator = models.ForeignKey(Indicator, models.DO_NOTHING, db_column='glucose_indicator', blank=True, null=True)
    state = models.ForeignKey('LiveState', models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_data'


class LiveState(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_state'


class NsActivity(models.Model):
    date = models.IntegerField(blank=True, null=True)
    sgv = models.IntegerField(blank=True, null=True)
    delta = models.IntegerField()
    systime = models.DateTimeField(db_column='sysTime', blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(max_length=30, blank=True, null=True)
    direction = models.CharField(max_length=20, blank=True, null=True)
    utcoffset = models.IntegerField(db_column='utcOffset', blank=True, null=True)  # Field name made lowercase.
    state = models.ForeignKey(ActivityState, models.DO_NOTHING, db_column='state', blank=True, null=True)
    when = models.DateTimeField()
    who = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ns_activity'


class Privacy(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    terms = models.IntegerField()
    advertising = models.IntegerField()
    partners = models.IntegerField()
    research = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'privacy'
        unique_together = (('id', 'user'),)


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
    verified = models.IntegerField()
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
    next_step = models.PositiveSmallIntegerField()
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

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('id', 'email'),)


class User2ActivityLog(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    activity_log = models.ForeignKey(ActivityLog, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_2_activity_log'


class User2ActivityRecommended(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    activity_recommended = models.ForeignKey(ActivityRecommended, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_2_activity_recommended'


class User2Forecast(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    forecast = models.ForeignKey(Forecast, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_2_forecast'


class User2Glucose(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    glucose = models.ForeignKey(Glucose, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_2_glucose'


class User2Livedata(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    livedata = models.ForeignKey(LiveData, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_2_livedata'
