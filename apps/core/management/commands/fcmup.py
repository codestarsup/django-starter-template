import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, "apps/core/fcm.py"), "w") as fcm:
            with open(os.path.join(settings.BASE_DIR, "apps/core/management/commands/fcm.txt"), "r") as fcm_txt:
                fcm.write(fcm_txt.read())
        self.stdout.write("FCM is up Check the core directory")
