from django.contrib import admin
from django.contrib.auth.models import (
    Group,
    User
)
from .models import (
    PartnerLogo,
    Form,
)
admin.site.unregister(Group) 
admin.site.unregister(User) 

admin.site.register(PartnerLogo)
admin.site.register(Form)
