from __future__ import absolut_import, unicode_literals
from argparse import Namespace
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'core.setting')

app = Celery('core')

app.config_from_objetct('django.conf:settings', Namespace='CELERY')

app.autodiscover_tasks()

@app.tasks(bind=True)
def debug_task(self):
    print('Request: (0!r)'.format(self.request))