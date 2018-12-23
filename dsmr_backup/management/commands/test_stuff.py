from django.core.management.base import BaseCommand

import dsmr_backup.services.email


class Command(BaseCommand):
    def handle(self, **options):
        dsmr_backup.services.email.send_backup()
