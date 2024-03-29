'''
Command that let Django to be waiting until db is available
'''
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        '''Command Entrypoint'''
        self.stdout.write('Waiting for database...')
        db_up = False

        while not db_up:

            try:
                self.check(databases=['default'])
                db_up = True

            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, wait for 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is avalaible!'))
