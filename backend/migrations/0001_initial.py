# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.CharField(max_length=30)),
                ('exname', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('typ', models.CharField(max_length=10)),
            ],
        ),
    ]
