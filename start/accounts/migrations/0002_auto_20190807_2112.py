# Generated by Django 2.2.4 on 2019-08-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='studyuser',
            name='major',
        ),
        migrations.AddField(
            model_name='studyuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studyuser',
            name='img_profile',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user'),
        ),
        migrations.AddField(
            model_name='studyuser',
            name='nickname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studyuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]