from django.contrib import admin
from .models import (
    Counter,
    Faculty,
    Partner,
    PartnerType,
    Program,
)
# Register your models here.
admin.site.register(Counter)

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

class FacultyAdmin(admin.ModelAdmin):
    list_display = (
        'text', 
        'created', 
        'updated'
    )
    list_filter = (
        'language',
    )
    search_fields = (
        "text",
    )

admin.site.register(Faculty, FacultyAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'created', 
        'updated'
    )
    list_filter = (
        'language',
    )
    search_fields = (
        "title",
    )
admin.site.register(Program, ProgramAdmin)