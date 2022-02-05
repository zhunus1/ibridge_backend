from django.db import models
from countries.models import Country
from django.utils.translation import *

# Create your models here.
class PartnerType(models.Model):
    title = models.CharField(
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

        verbose_name = ugettext_lazy("Partner Type")
        verbose_name_plural = ugettext_lazy("Partner Types")
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

class Counter(models.Model):
    counter_value = models.CharField(
        max_length=255,
    )

    counter_text = models.TextField(
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

        verbose_name = ugettext_lazy("Counter")
        verbose_name_plural = ugettext_lazy("Counters")
        ordering = ('-created',)

class Faculty(models.Model):
    text = models.CharField(
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

        verbose_name = ugettext_lazy("Faculty")
        verbose_name_plural = ugettext_lazy("Faculties")
        ordering = ('-created',)

    def __str__(self):
        return self.text

class Partner(models.Model):

    partner_image = models.ImageField(upload_to ='universities/image/')

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

    country = models.ForeignKey(
        to=Country, 
        on_delete=models.CASCADE
    )

    counters = models.ManyToManyField(
        to = Counter,
        related_name='partners'
    )

    about_text = models.TextField(
        blank=True,
    )

    about_video_url = models.URLField()

    faculties = models.ManyToManyField(
        to = Faculty,
        related_name='partners'
    )

    partner_type = models.ForeignKey(
        to=PartnerType, 
        on_delete=models.CASCADE,
        related_name='partners'
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