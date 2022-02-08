# Generated by Django 3.2.9 on 2022-02-08 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0008_remove_partnertranslation_partner_type'),
        ('universities', '0005_alter_partner_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='universities.partnertype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnertype',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='partner_types', to='translations.translationlanguage'),
            preserve_default=False,
        ),
    ]