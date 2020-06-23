# Generated by Django 2.2 on 2020-06-17 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LiveData',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('glucoseUnit', models.CharField(max_length=10)),
                ('glucoseIndicator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.Indicator')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.User')),
            ],
        ),
    ]
