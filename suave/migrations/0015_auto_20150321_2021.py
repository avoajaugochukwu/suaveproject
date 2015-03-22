# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0014_order_fabric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=3)),
                ('cost', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fabric',
            name='cost',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fabric',
            name='pattern',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fabric',
            name='sex',
            field=models.CharField(max_length=2, null=True),
            preserve_default=True,
        ),
    ]
