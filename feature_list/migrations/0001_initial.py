# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'feature published', db_index=True)),
                ('description', models.TextField()),
                ('url', models.URLField(default=b'', blank=True)),
                ('lead_developer', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=140)),
            ],
        ),
    ]
