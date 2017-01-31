import requests
from models import OauthCredentials
from OauthManager import OauthManager
import json


class Messenger:
    def __init__(self, card, roomId, attach_to=False, message_id=""):
        self.roomId = roomId
        self.message = ""
        self.attach_to = attach_to
        self.message_id = message_id
        self.auth_token = OauthCredentials.objects.filter(roomId__exact=self.roomId)[0].access_token
        self.headers = {'Content-Type': 'application/json'}
        self.card = card
        self.url_payload = {"auth_token": "{}".format(self.auth_token)}
        self.data = {
            'message': '{}'.format(self.card['activity']['html'],
            'card': self.card,
            'attach_to': '{}'.format(self.message_id),
            'message_format': 'html',
        }
        self.host = 'https://www.hipchat.com/v2/room/{}/notification'.format(self.roomId)

    def send_notification(self):
        r = requests.post(self.host, params=self.url_payload, data=json.dumps(self.data), headers=self.headers)
        print r.status_code
        print r.url
        if str(r.status_code) == '401':
            oauth = OauthManager(self.roomId)
            oauth.request_access_token()
            oauth.assign_access_token()   
            requests.post(self.host, params=self.url_payload, data=json.dumps(self.data), headers=self.headers)
