# Generated by Django 4.2.7 on 2023-11-29 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_product_names_alter_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='names',
        ),
    ]
