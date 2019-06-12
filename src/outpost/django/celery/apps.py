import logging

from django.apps import AppConfig
from .celery import app

logger = logging.getLogger(__name__)


class CeleryConfig(AppConfig):
    name = __package__
    verbose_name = "Celery"

    def ready(self):
        logger.info(f'Loaded celery instance {app.main}')
