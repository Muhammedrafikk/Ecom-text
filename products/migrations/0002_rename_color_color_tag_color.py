# Generated by Django 4.2.7 on 2023-11-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='tag_color',
        ),
    ]
