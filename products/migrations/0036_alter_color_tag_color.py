# Generated by Django 4.2.7 on 2023-12-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_delete_addprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='tag_color',
            field=models.CharField(choices=[('#b71c1c', 'Red'), ('#1b5e20', 'Green'), ('#303f9f', 'Blue')], default='#b71c1c', max_length=7),
        ),
    ]
