# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tourist', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('comment', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
