# Generated by Django 4.1.13 on 2023-12-16 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_rename_id_products__id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='_id',
            new_name='id',
        ),
    ]
