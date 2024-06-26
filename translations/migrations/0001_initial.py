# Generated by Django 3.2.9 on 2022-02-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40)),
                ('country_name', models.CharField(max_length=255, verbose_name='Country name')),
                ('banner_title', models.CharField(max_length=255, verbose_name='Banner title')),
                ('banner_sub_title', models.TextField(blank=True, verbose_name='Banner subtitle')),
                ('about_text', models.TextField(blank=True, verbose_name='About text')),
                ('advantage_1', models.TextField(blank=True, verbose_name='Advantage 1')),
                ('advantage_2', models.TextField(blank=True, verbose_name='Advantage 2')),
                ('advantage_3', models.TextField(blank=True, verbose_name='Advantage 3')),
                ('advantage_4', models.TextField(blank=True, verbose_name='Advantage 4')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Country translation',
                'verbose_name_plural': 'Country translations',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PartnerTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=255, verbose_name='Partner name')),
                ('foundation_year', models.CharField(max_length=255, verbose_name='Foundation year')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('payment', models.CharField(max_length=255, verbose_name='Payment')),
                ('about_text', models.TextField(blank=True, verbose_name='About text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Partner translation',
                'verbose_name_plural': 'Partner translations',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TranslationLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Translation language',
                'verbose_name_plural': 'Translation languages',
                'ordering': ('-created',),
            },
        ),
    ]
