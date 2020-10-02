# Generated by Django 3.0.7 on 2020-10-01 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200817_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glucose_low_limit', models.IntegerField()),
                ('glucose_high_limit', models.IntegerField()),
                ('mode', models.IntegerField()),
                ('very_high_alarm', models.BooleanField()),
                ('high_alarm', models.BooleanField()),
                ('low_alarm', models.BooleanField()),
                ('very_low_alarm', models.BooleanField()),
                ('units', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'prefs',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='source',
            field=models.ForeignKey(db_column='source_id', on_delete=django.db.models.deletion.CASCADE, to='webapp.Source'),
        ),
        migrations.AddField(
            model_name='profile',
            name='prefs',
            field=models.ForeignKey(db_column='prefs_id', default=0, on_delete=django.db.models.deletion.CASCADE, to='webapp.Preferences'),
            preserve_default=False,
        ),
    ]