# Generated by Django 4.2.7 on 2023-11-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_wishlist_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
