from django.db import models
from countries.models import Country
from django.utils.translation import *

# Create your models here.
class PartnerType(models.Model):
    language = models.ForeignKey(
        to = 'translations.TranslationLanguage', 
        on_delete = models.CASCADE,
        related_name='partner_types',
        verbose_name = ugettext_lazy("Language"),
    )

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

        verbose_name = ugettext_lazy("Partner type")
        verbose_name_plural = ugettext_lazy("Partner types")
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

class Counter(models.Model):
    counter_value = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Counter value"),
    )

    counter_text = models.TextField(
        blank=True,
        verbose_name = ugettext_lazy("Counter text"),
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

        verbose_name = ugettext_lazy("Counter")
        verbose_name_plural = ugettext_lazy("Counters")
        ordering = ('-created',)
    
    def __str__(self):
        return '%s - %s' % (self.counter_value, self.counter_text)

class Faculty(models.Model):
    language = models.ForeignKey(
        to = 'translations.TranslationLanguage', 
        on_delete = models.CASCADE,
        related_name='faculties',
        verbose_name = ugettext_lazy("Language"),
    )

    text = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Text"),
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

        verbose_name = ugettext_lazy("Faculty")
        verbose_name_plural = ugettext_lazy("Faculties")
        ordering = ('-created',)

    def __str__(self):
        return self.text

class Program(models.Model):
    language = models.ForeignKey(
        to = 'translations.TranslationLanguage', 
        on_delete = models.CASCADE,
        related_name='programs',
        verbose_name = ugettext_lazy("Language"),
    )

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

        verbose_name = ugettext_lazy("Program")
        verbose_name_plural = ugettext_lazy("Programs")
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Partner(models.Model):

    partner_name = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Partner name"),
    )

    country = models.ForeignKey(
        to=Country, 
        on_delete=models.CASCADE,
        related_name='partners',
        verbose_name = ugettext_lazy("Country"),
    )

    partner_image = models.ImageField(
        upload_to ='universities/partners/image',
        verbose_name = ugettext_lazy("Partner image"),
    )

    about_video_url = models.URLField(verbose_name = ugettext_lazy("About video URL"),)

    about_image = models.ImageField(
        upload_to ='universities/partners/about/',
        verbose_name = ugettext_lazy("About image"),
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

        verbose_name = ugettext_lazy("Partner")
        verbose_name_plural = ugettext_lazy("Partners")
        ordering = ('-created',)

    def __str__(self):
        return self.partner_name