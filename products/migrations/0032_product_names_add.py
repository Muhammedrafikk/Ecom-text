# Generated by Django 4.2.7 on 2023-12-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_remove_product_names_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='names_add',
            field=models.CharField(default=12, max_length=150),
            preserve_default=False,
        ),
    ]
