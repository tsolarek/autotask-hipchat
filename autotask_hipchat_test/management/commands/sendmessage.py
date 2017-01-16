from django.core.management.base import BaseCommand, CommandError
from autotask_hipchat_test.Messenger import Messenger
from autotask_hipchat_test.models import OauthCredentials

class Command(BaseCommand):
    help = 'Create Hipchat webhook'

    def handle(self, *args, **options):
        messenger = Messenger(message='Hello!', roomId=3396503)
        messenger.send_notification()