from __future__ import absolute_import

import os

from celery import Celery
from core.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

app = Celery("real_estate_api")

app.config_from_object("core.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
