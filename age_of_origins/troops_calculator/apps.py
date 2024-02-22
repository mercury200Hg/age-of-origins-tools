import csv

from django.apps import AppConfig


class TroopsCalculatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'troops_calculator'

    def ready(self):
        pass
