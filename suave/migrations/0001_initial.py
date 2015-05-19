# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('preference', models.CharField(max_length=40)),
                ('sex', models.CharField(default=b' ', max_length=2, choices=[(b'F', b'F'), (b'M', b'M')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField(null=True)),
                ('sex', models.CharField(max_length=2, null=True)),
                ('pattern', models.CharField(max_length=150, null=True)),
                ('image_url', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabric', models.CharField(max_length=50, null=True)),
                ('style', models.CharField(max_length=100, null=True)),
                ('main_order_id', models.CharField(max_length=15, null=True)),
                ('details', models.CharField(max_length=250, null=True)),
                ('delivery_option', models.CharField(max_length=100, null=True)),
                ('service_option', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(default=b' ', max_length=2)),
                ('status', models.CharField(default=b'OPEN', max_length=20)),
                ('cost', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('client', models.ForeignKey(to='suave.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=3)),
                ('cost', models.IntegerField(default=0)),
                ('pattern', models.CharField(max_length=150, null=True)),
                ('image_url', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tailor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(default=0)),
                ('phone_number', models.CharField(default=0, max_length=13)),
                ('address', models.CharField(max_length=300, null=True)),
                ('specialty', models.CharField(max_length=300, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
        migrations.AddField(
            model_name='order',
            name='tailor',
            field=models.ForeignKey(to='suave.Tailor', null=True),
            preserve_default=True,
        ),
    ]
