# Generated by Django 4.2.7 on 2023-11-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_color_add_color_alter_color_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='add_color',
            field=models.CharField(choices=[('#FF0000', 'Red'), ('#00FF00', 'Green'), ('#0000FF', 'Blue'), ('#FFC0CB', 'Yellow')], default='danger', max_length=120),
        ),
        migrations.AlterField(
            model_name='color',
            name='tag_color',
            field=models.CharField(choices=[('#FF0000', 'Red'), ('#00FF00', 'Green'), ('#0000FF', 'Blue'), ('#FFC0CB', 'Yellow')], default='RED', max_length=7),
        ),
    ]
