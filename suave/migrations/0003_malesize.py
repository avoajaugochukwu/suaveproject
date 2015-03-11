# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0002_auto_20150311_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaleSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center_back', models.IntegerField(default=0)),
                ('chest', models.IntegerField(default=0)),
                ('inside_leg', models.IntegerField(default=0)),
                ('sleeve', models.IntegerField(default=0)),
                ('waist', models.IntegerField(default=0)),
                ('client', models.ForeignKey(to='suave.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
