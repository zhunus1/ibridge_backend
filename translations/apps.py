from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class TranslationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'translations'
    verbose_name = ugettext_lazy('translations')
