# Generated by Django 4.2.7 on 2023-11-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_color_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='add_color',
            field=models.CharField(choices=[('danger', 'Red'), ('success', 'Green'), ('info', 'Blue'), ('warning', 'Yellow')], default='danger', max_length=120),
        ),
        migrations.AlterField(
            model_name='color',
            name='tag_color',
            field=models.CharField(choices=[('danger', 'Red'), ('success', 'Green'), ('info', 'Blue'), ('warning', 'Yellow')], default='RED', max_length=7),
        ),
    ]