# Generated by Django 3.0.6 on 2020-05-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20200531_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
