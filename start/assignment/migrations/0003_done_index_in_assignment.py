# Generated by Django 2.2.4 on 2019-08-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_assignment_index_in_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='done',
            name='index_in_assignment',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]