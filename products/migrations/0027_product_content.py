# Generated by Django 4.2.7 on 2023-11-30 05:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_rename_name_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=tinymce.models.HTMLField(default=12),
            preserve_default=False,
        ),
    ]