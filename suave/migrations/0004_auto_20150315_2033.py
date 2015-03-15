# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0003_malesize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bust', models.IntegerField(default=0)),
                ('center_back', models.IntegerField(default=0)),
                ('chest', models.IntegerField(default=0)),
                ('inside_leg', models.IntegerField(default=0)),
                ('hips', models.IntegerField(default=0)),
                ('sleeve', models.IntegerField(default=0)),
                ('waist', models.IntegerField(default=0)),
                ('client', models.ForeignKey(to='suave.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='malesize',
            name='client',
        ),
        migrations.DeleteModel(
            name='MaleSize',
        ),
        migrations.RemoveField(
            model_name='client',
            name='size',
        ),
    ]
