# Generated by Django 4.2.7 on 2023-11-23 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_color_add_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='tag_color',
            field=models.CharField(choices=[('#b71c1c', 'Red'), ('#1b5e20', 'Green'), ('#303f9f', 'Blue'), ('#ffd600', 'Yellow')], default='#b71c1c', max_length=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='prices',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color')),
            ],
        ),
    ]