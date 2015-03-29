# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size_value', models.CharField(max_length=15)),
                ('collar', models.CharField(max_length=10)),
                ('waist', models.CharField(max_length=10)),
                ('hips', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='sizetable',
            field=models.ForeignKey(to='suave.SizeTable', null=True),
            preserve_default=True,
        ),
    ]
