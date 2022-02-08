from django.contrib import admin
from .models import (
    Counter,
    Faculty,
    Partner,
    PartnerType,
)
# Register your models here.
admin.site.register(Counter)
admin.site.register(Faculty)

class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'partner_name', 
        'country', 
        'created', 
        'updated'
    )
    list_filter = (
        'country__country_name',
    )
    search_fields = (
        "partner_name",
    )
admin.site.register(Partner, PartnerAdmin)

class PartnerTypeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'language', 
        'created', 
        'updated'
    )
    list_filter = (
        'language',
    )
    search_fields = (
        "title",
    )
admin.site.register(PartnerType, PartnerTypeAdmin)
