# Generated by Django 4.1.13 on 2023-12-19 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_rename_id_contact_contact_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='prod_id',
            new_name='id',
        ),
    ]
