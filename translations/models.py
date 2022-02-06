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
    language = models.CharField(
        max_length=255,
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

class CountryTranslation(models.Model):
    language = models.ForeignKey(
        to = TranslationLanguage, 
        on_delete = models.CASCADE,
        related_name='country_translations'
    )

    country = models.ForeignKey(
        to = Country, 
        on_delete = models.CASCADE
    )

    country_name = models.CharField(
        max_length=255,
    )

    banner_title = models.CharField(
        max_length=255,
    )
    
    banner_sub_title = models.TextField(
        blank=True,
    )

    about_text = models.TextField(
        blank=True,
    )

    advantage_1 = models.TextField(
        blank=True,
    )

    advantage_2 = models.TextField(
        blank=True,
    )

    advantage_3 = models.TextField(
        blank=True,
    )

    advantage_4 = models.TextField(
        blank=True,
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

    partner = models.ForeignKey(
        to = Partner, 
        on_delete = models.CASCADE
    )

    language = models.ForeignKey(
        to = TranslationLanguage, 
        on_delete = models.CASCADE,
        related_name='partner_translations'
    )

    partner = models.ForeignKey(
        to = Partner, 
        on_delete = models.CASCADE
    )

    partner_name = models.CharField(
        max_length=255,
    )

    foundation_year = models.CharField(
        max_length=255,
    )

    location = models.CharField(
        max_length=255,
    )

    payment = models.CharField(
        max_length=255,
    )

    about_text = models.TextField(
        blank=True,
    )

    faculties = models.ManyToManyField(
        to = Faculty,
        related_name='partner_translations'
    )

    partner_type = models.ForeignKey(
        to=PartnerType, 
        on_delete=models.CASCADE,
        related_name='partner_translations'
    )

    counters = models.ManyToManyField(
        to = Counter,
        related_name='partner_translations'
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