# Generated by Django 4.1.13 on 2023-12-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=10),
        ),
    ]