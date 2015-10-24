# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=30)),
            ],
        ),
    ]
