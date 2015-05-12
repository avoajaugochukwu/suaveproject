# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0002_tailor_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='soft_delete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
