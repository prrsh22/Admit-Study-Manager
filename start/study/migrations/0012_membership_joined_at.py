# Generated by Django 2.2.4 on 2019-08-23 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0011_auto_20190823_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='joined_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 11, 0)),
        ),
    ]