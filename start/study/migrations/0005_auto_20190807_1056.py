# Generated by Django 2.2.4 on 2019-08-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_group_group_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_code',
            field=models.CharField(max_length=20),
        ),
    ]