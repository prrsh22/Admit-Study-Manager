# Generated by Django 2.2.4 on 2019-08-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studypost', '0002_auto_20190815_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='homework',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]