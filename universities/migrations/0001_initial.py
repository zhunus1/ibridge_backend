# Generated by Django 3.2.9 on 2022-02-10 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_value', models.CharField(max_length=255, verbose_name='Counter value')),
                ('counter_text', models.TextField(blank=True, verbose_name='Counter text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='translations.translationlanguage', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_types', to='translations.translationlanguage', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Partner type',
                'verbose_name_plural': 'Partner types',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=255, verbose_name='Partner name')),
                ('partner_image', models.ImageField(upload_to='universities/partners/image', verbose_name='Partner image')),
                ('about_video_url', models.URLField(verbose_name='About video URL')),
                ('about_image', models.ImageField(upload_to='universities/partners/about/', verbose_name='About image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='countries.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='translations.translationlanguage', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
                'ordering': ('-created',),
            },
        ),
    ]
