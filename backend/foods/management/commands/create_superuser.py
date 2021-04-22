from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create Super User'

    def create_superuser(self, username, password):
        User.objects.create_superuser(
            username, f'{username}@example.com', password)

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        self.create_superuser(username, password)
        self.stdout.write(f'Create superuser: {username}')
