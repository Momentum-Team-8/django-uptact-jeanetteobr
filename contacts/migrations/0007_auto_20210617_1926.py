# Generated by Django 3.2.4 on 2021-06-17 19:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20210617_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 19, 25, 57, 13407, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
