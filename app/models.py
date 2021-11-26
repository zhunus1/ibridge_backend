from django.db import models
from django.utils.translation import *

# Create your models here.

class PartnerLogo(models.Model):
    image = models.ImageField(upload_to ='logos/')
    name = models.CharField(
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

        verbose_name = ugettext_lazy("Partner Logo")
        verbose_name_plural = ugettext_lazy("Partners Logo")
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Form(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    phone_number = models.CharField(
        max_length=255,
    )
    comments = models.TextField()

    created = models.DateTimeField(
        verbose_name = ugettext_lazy("Created"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = ugettext_lazy("Updated"),
        auto_now = True,
    )
    
    class Meta:

        verbose_name = ugettext_lazy("Client Form")
        verbose_name_plural = ugettext_lazy("Client Forms")
        ordering = ('-created',)

    def __str__(self):
        return self.phone
