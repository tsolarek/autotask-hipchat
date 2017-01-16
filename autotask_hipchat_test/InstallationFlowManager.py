# Handles the creation of OauthCredentials database entry during application installation.

from models import OauthCredentials


class InstallationFlowManager:

    def __init__(self, installation_call_back):
        self.oauthId = installation_call_back['oauthId']
        self.roomId = installation_call_back['roomId']
        self.groupId = installation_call_back['groupId']
        self.oauthSecret = installation_call_back['oauthSecret']

    def create_oauth_credentials(self):
        credentials = OauthCredentials()

        credentials.oauthId = self.oauthId
        credentials.roomId = self.roomId
        credentials.groupId = self.groupId
        credentials.oauthSecret = self.oauthSecret

        credentials.save()

    def delete_oauth_credentials(self):
        credentials = OauthCredentials.objects.filter(roomId__exact=self.roomId, groupId__exact=self.groupId)

        credentials.delete()



