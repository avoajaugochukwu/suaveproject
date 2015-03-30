# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0002_auto_20150329_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 13, 35, 50, 891000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
