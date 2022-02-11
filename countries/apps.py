from django.apps import AppConfig
from django.utils.translation import ugettext_lazy

class CountriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = ('countries')
    verbose_name = ugettext_lazy('countries')
