from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "bernie_calc.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import bernie_calc.users.signals  # noqa F401
        except ImportError:
            pass
