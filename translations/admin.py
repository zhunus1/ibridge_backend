from django.contrib import admin
from .models import (
    TranslationLanguage,
    CountryTranslation,
    PartnerTranslation
)
# Register your models here.
admin.site.register(TranslationLanguage)
admin.site.register(CountryTranslation)
admin.site.register(PartnerTranslation)
