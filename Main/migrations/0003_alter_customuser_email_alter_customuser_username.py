# Generated by Django 5.0.1 on 2024-01-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_draft_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, verbose_name='username'),
        ),
    ]