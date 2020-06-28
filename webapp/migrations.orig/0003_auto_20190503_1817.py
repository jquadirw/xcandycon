# Generated by Django 2.2 on 2019-05-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_frame_function'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correlation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xcolumns', models.CharField(choices=[('Column A', 'Column A'), ('Column B', 'Column B'), ('Column C', 'Column C')], max_length=100)),
                ('ycolumns', models.CharField(choices=[('Column A', 'Column A'), ('Column B', 'Column B'), ('Column C', 'Column C')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='frame',
            name='files',
        ),
    ]