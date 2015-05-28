# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Room Name')),
                ('image', models.ImageField(verbose_name='Picture', upload_to='img/')),
                ('price', models.IntegerField(verbose_name='Cost per night')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
            ],
        ),
    ]
