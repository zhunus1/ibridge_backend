from django.db import models
from universities.models import (
    Partner,
    Faculty,
    Counter,
    PartnerType
)
from countries.models import Country
from django.utils.translation import *

# Create your models here.
class TranslationLanguage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Title"),
    )

    created = models.DateTimeField(
        verbose_name = ugettext_lazy("Created"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = ugettext_lazy("Updated"),
        auto_now = True,
    )

    class Meta:

        verbose_name = ugettext_lazy("Translation Language")
        verbose_name_plural = ugettext_lazy("Translation Languages")
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

class CountryTranslation(models.Model):
    language = models.ForeignKey(
        to = TranslationLanguage, 
        on_delete = models.CASCADE,
        related_name='country_translations',
        verbose_name = ugettext_lazy("Language"),
    )

    country = models.ForeignKey(
        to = Country, 
        on_delete = models.CASCADE,
        related_name='country_translations',
        verbose_name = ugettext_lazy("Country"),
    )

    country_name = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Country Name"),
    )

    banner_title = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Banner Title"),
    )

    banner_sub_title = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("Banner Subtitle"),
    )

    about_text = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("About Text"),
    )

    advantage_1 = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("Advantage 1"),
    )

    advantage_2 = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("Advantage 2"),
    )

    advantage_3 = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("Advantage 3"),
    )

    advantage_4 = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("Advantage 4"),
    )

    created = models.DateTimeField(
        verbose_name = ugettext_lazy("Created"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = ugettext_lazy("Updated"),
        auto_now = True,
    )

    class Meta:

        verbose_name = ugettext_lazy("Country Translation")
        verbose_name_plural = ugettext_lazy("Country Translations")
        ordering = ('-created',)

    def __str__(self):
        return self.country_name

class PartnerTranslation(models.Model):

    language = models.ForeignKey(
        to = TranslationLanguage, 
        on_delete = models.CASCADE,
        related_name='partner_translations',
        verbose_name = ugettext_lazy("Language"),
    )
    
    partner_type = models.ForeignKey(
        to=PartnerType, 
        on_delete=models.CASCADE,
        related_name='partner_translations',
        verbose_name = ugettext_lazy("Partner Type"),
    )

    partner = models.ForeignKey(
        to = Partner, 
        on_delete = models.CASCADE,
        related_name='partner_translations',
        verbose_name = ugettext_lazy("Partner"),
    )

    partner_name = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Partner Name"),
    )

    foundation_year = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Foundation Year"),
    )

    location = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Location"),
    )

    payment = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Payment"),
    )

    about_text = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("About Text"),
    )

    faculties = models.ManyToManyField(
        to = Faculty,
        related_name='partner_translations',
        verbose_name = ugettext_lazy("Faculties"),
    )

    counters = models.ManyToManyField(
        to = Counter,
        related_name='partner_translations',
        verbose_name = ugettext_lazy("Counters"),
    )

    created = models.DateTimeField(
        verbose_name = ugettext_lazy("Created"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = ugettext_lazy("Updated"),
        auto_now = True,
    )

    class Meta:

        verbose_name = ugettext_lazy("Partner Translation")
        verbose_name_plural = ugettext_lazy("Partner Translations")
        ordering = ('-created',)

    def __str__(self):
        return self.partner_name 