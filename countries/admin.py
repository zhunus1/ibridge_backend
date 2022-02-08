from django.contrib import admin
from .models import (
    Country,
    AboutImage,
)


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'country_name', 
        'created', 
        'updated'
    )
    search_fields = (
        "country_name",
    )


admin.site.register(AboutImage)

admin.site.register(Country, CountryAdmin)
