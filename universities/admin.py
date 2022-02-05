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
admin.site.register(Partner)
admin.site.register(PartnerType)