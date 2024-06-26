# Generated by Django 3.2.9 on 2022-02-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_alter_country_seo_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='country_slug',
            field=models.SlugField(default='country', help_text="Define the country's URL slug. Only lowercase and _ instead of space.", max_length=40, verbose_name='Country slug'),
        ),
    ]
