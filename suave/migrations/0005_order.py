# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0004_auto_20150315_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fabric', models.IntegerField(null=True)),
                ('details', models.CharField(max_length=250, null=True)),
                ('delivery_option', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(default=b' ', max_length=2)),
                ('status', models.CharField(default=b'', max_length=20)),
                ('cost', models.IntegerField(default=0)),
                ('client', models.ForeignKey(to='suave.Client')),
                ('size', models.ForeignKey(to='suave.Size', null=True)),
                ('tailor', models.ForeignKey(to='suave.Tailor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
