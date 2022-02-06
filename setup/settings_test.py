from setup.settings import *  # noqa
import warnings

warnings.filterwarnings("ignore")

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

MIGRATION_MODULES = {
    "auth": None,
    "admin": None,
    "contenttypes": None,
    "sessions": None,
    "cronos": None,
}
