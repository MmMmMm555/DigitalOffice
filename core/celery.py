from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

# app.config_from_object(settings)
app.autodiscover_tasks()
