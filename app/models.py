from django.db import models
from django.utils.translation import *
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class PartnerLogo(TranslatableModel):
    translations = TranslatedFields(
        image = models.ImageField(upload_to ='logos/'),
        name = models.CharField(max_length=255),
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

class Counter(TranslatableModel):
    translations = TranslatedFields(
        number = models.IntegerField(),
        name = models.CharField(
            max_length=255,
        ),
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
        return self.name


class Country(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(
            max_length=255,
        ),
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

        verbose_name = ugettext_lazy("Study place")
        verbose_name_plural = ugettext_lazy("Study places")
        ordering = ('-created',)

    def __str__(self):
        return self.name

class University(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(
            max_length=255,
        ),
        country = models.ForeignKey(
            verbose_name= ugettext_lazy("Country"),
            to=Country,
            related_name='universities',
            on_delete=models.CASCADE,
        )
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

        verbose_name = ugettext_lazy("University")
        verbose_name_plural = ugettext_lazy("Universities")
        ordering = ('-created',)

    def __str__(self):
        return self.name
