from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Delete Super User'

    def delete_superuser(self, username):
        User.objects.get(username=username, is_superuser=True).delete()

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        try:
            self.delete_superuser(username)
        except UserModel.DoesNotExist:
            raise CommandError(
                'User {} does not exist'.format(
                    username)
            )
        self.stdout.write(f'Delete user: {username}')
