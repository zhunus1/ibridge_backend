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
admin.site.register(PartnerType)

class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'partner_name', 
        'partner_type', 
        'created', 
        'updated'
    )
    list_filter = (
        'country__country_name',
        'partner_type__title',
    )
    search_fields = (
        "partner_name",
    )


admin.site.register(Partner, PartnerAdmin)
