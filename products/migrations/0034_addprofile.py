# Generated by Django 4.2.7 on 2023-12-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_alter_product_color_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
