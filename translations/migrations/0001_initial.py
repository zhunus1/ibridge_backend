# Generated by Django 3.2.9 on 2022-02-06 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0003_auto_20220206_1137'),
        ('universities', '0004_auto_20220206_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Translation Language',
                'verbose_name_plural': 'Translation Languages',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PartnerTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=255)),
                ('foundation_year', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('payment', models.CharField(max_length=255)),
                ('about_text', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('counters', models.ManyToManyField(related_name='partner_translations', to='universities.Counter')),
                ('faculties', models.ManyToManyField(related_name='partner_translations', to='universities.Faculty')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_translations', to='translations.translationlanguage')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universities.partner')),
                ('partner_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_translations', to='universities.partnertype')),
            ],
            options={
                'verbose_name': 'Partner Translation',
                'verbose_name_plural': 'Partner Translations',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='CountryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('banner_title', models.CharField(max_length=255)),
                ('banner_sub_title', models.TextField(blank=True)),
                ('about_text', models.TextField(blank=True)),
                ('advantage_1', models.TextField(blank=True)),
                ('advantage_2', models.TextField(blank=True)),
                ('advantage_3', models.TextField(blank=True)),
                ('advantage_4', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_translations', to='translations.translationlanguage')),
            ],
            options={
                'verbose_name': 'Country Translation',
                'verbose_name_plural': 'Country Translations',
                'ordering': ('-created',),
            },
        ),
    ]
