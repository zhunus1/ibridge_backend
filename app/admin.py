from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    PartnerLogo,
    Counter,
    Country,
    University,
)

admin.site.register(PartnerLogo, TranslatableAdmin)
admin.site.register(Counter, TranslatableAdmin)
admin.site.register(Country, TranslatableAdmin)
admin.site.register(University, TranslatableAdmin)
