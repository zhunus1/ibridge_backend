from django.db import models
from django.utils.translation import *

# Create your models here.
class AboutImage(models.Model):
    image = models.ImageField(upload_to ='countries/about/')
    
    created = models.DateTimeField(
        verbose_name = ugettext_lazy("Created"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = ugettext_lazy("Updated"),
        auto_now = True,
    )

    class Meta:

        verbose_name = ugettext_lazy("About Image")
        verbose_name_plural = ugettext_lazy("About Images")
        ordering = ('-created',)

class Country(models.Model):
    country_name = models.CharField(
        max_length=255,
    )

    banner_title = models.CharField(
        max_length=255,
    )
    
    banner_sub_title = models.TextField(
        blank=True,
    )

    banner_image = models.ImageField(upload_to ='countries/banner/')

    about_text = models.TextField(
        blank=True,
    )

    about_image = models.ManyToManyField(
        to = AboutImage,
        related_name='countries'
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

        verbose_name = ugettext_lazy("Country")
        verbose_name_plural = ugettext_lazy("Countries")
        ordering = ('-created',)

    def __str__(self):
        return self.country_name