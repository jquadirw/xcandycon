# Generated by Django 3.0.7 on 2020-08-17 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Source'),
        ),
    ]
