from django.contrib import admin
from .models import (
    Country,
    AboutImage,
)

admin.site.register(AboutImage)

class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'country_name', 
        'created', 
        'updated'
    )
    search_fields = (
        "country_name",
    )

admin.site.register(Country, CountryAdmin)
