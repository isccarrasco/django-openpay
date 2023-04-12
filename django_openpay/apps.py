from django.apps import AppConfig
from . import gettext_lazy


class DjangoOpenpayConfig(AppConfig):
    name = 'django_openpay'
    verbose_name = gettext_lazy('Django Openpay')
