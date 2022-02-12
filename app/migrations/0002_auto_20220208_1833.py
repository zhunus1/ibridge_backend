# Generated by Django 3.2.9 on 2022-02-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='form',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='form',
            name='phone_number',
            field=models.CharField(max_length=255, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='partnerlogo',
            name='image',
            field=models.ImageField(upload_to='logos/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='partnerlogo',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]