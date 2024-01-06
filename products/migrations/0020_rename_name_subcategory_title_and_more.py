# Generated by Django 4.2.7 on 2023-11-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_rename_title_subcategory_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_add',
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=12, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
