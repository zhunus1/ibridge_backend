from django.contrib import admin
from .models import (
    TranslationLanguage,
    CountryTranslation,
    PartnerTranslation
)
# Register your models here.
admin.site.register(TranslationLanguage)

class CountryTranslationAdmin(admin.ModelAdmin):
    list_display = (
        'country_name', 
        'language', 
        'created', 
        'updated'
    )
    list_filter = (
        'language__title',
        'country__country_name',
    )
    search_fields = (
        "country_name",
    )


admin.site.register(CountryTranslation, CountryTranslationAdmin)

class PartnerTranslationAdmin(admin.ModelAdmin):
    list_display = (
        'partner_name', 
        'language', 
        'created', 
        'updated'
    )
    list_filter = (
        'language__title',
        'partner__country__country_name',
    )
    search_fields = (
        "partner_name",
    )


admin.site.register(PartnerTranslation, PartnerTranslationAdmin)
