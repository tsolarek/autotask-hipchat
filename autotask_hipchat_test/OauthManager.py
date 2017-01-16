from models import OauthCredentials
import requests
from requests.auth import HTTPBasicAuth


class OauthManager:
    def __init__(self, room_id, grant_type="client_credentials", scope="send_notification"):
        self.url_payload = {"grant_type": "{}".format(grant_type), "scope": "{}".format(scope)}
        self.form_data = {u'Content-Type': u'application/x-www-form-urlencoded'}
        self.host = 'https://www.hipchat.com/v2/oauth/token'
        self.room_id = room_id
        self.oauthCredentials = OauthCredentials.objects.filter(roomId__exact=self.room_id)[0]
        self.oauthSecret = self.oauthCredentials.oauthSecret
        self.oauthId = self.oauthCredentials.oauthId

    def request_access_token(self):
        r = requests.post(self.host, auth=HTTPBasicAuth(self.oauthId, self.oauthSecret), params=self.url_payload, data=self.form_data)
        self.response = r.json()
        print self.response

    def assign_access_token(self):
        self.oauthCredentials.access_token = self.response['access_token']
        self.oauthCredentials.save()

    def test_token(self):
        auth_token = self.oauthCredentials.access_token
        test_payload = {"auth_token": "{}".format(auth_token), "auth_test": "true"}
        r = requests.get('https://www.hipchat.com/v2/room', params=test_payload)
        print r.url
        print r.text
