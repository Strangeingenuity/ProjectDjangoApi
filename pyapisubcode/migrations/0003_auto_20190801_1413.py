# Generated by Django 2.2.3 on 2019-08-01 19:13

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pyapisubcode', '0002_auto_20190801_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='body',
            field=models.TextField(default=datetime.datetime(2019, 8, 1, 19, 13, 15, 981524, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
