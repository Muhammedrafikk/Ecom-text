# Generated by Django 4.2.7 on 2023-11-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_rename_name_subcategory_title_and_more'),
        ('orders', '0006_wishlistitem_color_alter_wishlistitem_prices_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='color',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='prices',
        ),
        migrations.AlterField(
            model_name='wishlistitem',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]