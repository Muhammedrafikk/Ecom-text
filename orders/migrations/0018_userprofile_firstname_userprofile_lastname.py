# Generated by Django 4.2.7 on 2023-12-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_userprofile_email_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
