# Generated by Django 3.2.9 on 2022-02-08 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_country_country_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='about_image',
            new_name='about_images',
        ),
    ]