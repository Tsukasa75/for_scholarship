# Generated by Django 5.0.1 on 2024-02-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_merge_20240206_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='auth_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]