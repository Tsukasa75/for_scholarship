# Generated by Django 5.0.1 on 2024-02-18 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_rename_stripe_customer_id_customuser_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='product_id',
            new_name='stripe_customer_id',
        ),
    ]