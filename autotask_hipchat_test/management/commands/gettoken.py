from django.core.management.base import BaseCommand, CommandError
from autotask_hipchat_test.OauthManager import OauthManager
from autotask_hipchat_test.models import OauthCredentials

class Command(BaseCommand):
    help = 'Create Hipchat webhook'

    def handle(self, *args, **options):
        manager = OauthManager(144853)
        manager.request_access_token()
        manager.assign_access_token()



