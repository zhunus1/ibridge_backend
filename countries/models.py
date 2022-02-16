from django.db import models
from django.utils.translation import *

# Create your models here.
class AboutImage(models.Model):
    image = models.ImageField(
        upload_to ='countries/about/',
        verbose_name = ugettext_lazy("Image"),
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

        verbose_name = ugettext_lazy("About image")
        verbose_name_plural = ugettext_lazy("About images")
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.pk)

class Country(models.Model):
    country_logo = models.ImageField(
        upload_to ='countries/logo/',
        verbose_name = ugettext_lazy("Country logo"),
    )

    country_slug = models.SlugField(
        max_length=40,
        help_text=ugettext_lazy("Define the country's URL slug. Only lowercase and _ instead of space."),
        verbose_name = ugettext_lazy("Country slug"),
        default='country'
    )

    country_name = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Country name"),
    )

    banner_image = models.ImageField(
        upload_to ='countries/banner/',
        verbose_name = ugettext_lazy("Banner image"),
    )

    about_images = models.ManyToManyField(
        to = AboutImage,
        related_name='countries',
        verbose_name = ugettext_lazy("About images"),
    )

    seo_text = models.TextField(
        blank=True,
        null=True,
        verbose_name = ugettext_lazy("SEO text"),
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
        return str(self.country_name)