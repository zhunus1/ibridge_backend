# Generated by Django 3.2.9 on 2022-02-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211126_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]