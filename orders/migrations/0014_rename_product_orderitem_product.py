# Generated by Django 4.2.7 on 2023-11-29 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_rename_product_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='Product',
        ),
    ]