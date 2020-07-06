import os
import sys

from django.apps import AppConfig


class DsConfig(AppConfig):
    name = 'ds'

    def ready(self):
        if 'runserver' not in sys.argv:  # TODO возможно не запуститься через wsgi
            return True
        if os.environ.get('RUN_MAIN') == 'true':
            from ds import bot
            bot.start()
