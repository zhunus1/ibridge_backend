# Generated by Django 3.2.9 on 2022-02-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_auto_20220205_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_image',
            field=models.ImageField(default=1, upload_to='universities/image/'),
            preserve_default=False,
        ),
    ]
