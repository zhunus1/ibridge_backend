from django.contrib import admin
from .models import (
    Country,
    AboutImage,
)

admin.site.register(Country)
admin.site.register(AboutImage)
