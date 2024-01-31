from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {

    'check_delayed_results_at_23-58': {
        'task': 'apps.friday_tesis.tasks.check_delayed_results',
        'schedule': crontab(hour=23, minute=58),
    },

    'check_delayed_direction_results_at_23-58': {
        'task': 'apps.orders.tasks.check_delayed_direction_results',
        'schedule': crontab(hour=23, minute=58),
    },
}
