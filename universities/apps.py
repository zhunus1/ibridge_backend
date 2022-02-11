from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class UniversitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'universities'
    verbose_name = ugettext_lazy('universities')
