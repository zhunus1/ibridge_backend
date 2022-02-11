from django.db import models
from django.utils.translation import *

# Create your models here.

class PartnerLogo(models.Model):
    image = models.ImageField(
        upload_to ='logos/',
        verbose_name = ugettext_lazy("Logo"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Name"),
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
        verbose_name = ugettext_lazy("First Name"),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Last Name"),
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name = ugettext_lazy("Phone Number"),
    )
    comments = models.TextField(
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

        verbose_name = ugettext_lazy("Client Form")
        verbose_name_plural = ugettext_lazy("Client Forms")
        ordering = ('-created',)

    def __str__(self):
        return self.phone_number