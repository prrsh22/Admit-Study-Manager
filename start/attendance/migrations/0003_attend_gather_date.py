# Generated by Django 2.2.4 on 2019-08-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20190811_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='attend',
            name='gather_date',
            field=models.DateField(default=None, verbose_name='모임날짜'),
            preserve_default=False,
        ),
    ]
