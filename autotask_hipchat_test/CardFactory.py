import binascii
import os


class CardFactory:
    def __init__(self, ticket_info):
        self.ticket_number = ticket_info['ticket_number']
        self.ticket_title = ticket_info['ticket_title']
        self.ticket_id = ticket_info['ticket_id']
        self.ticket_priority = ticket_info['ticket_priority']
        self.priority_icon_url = ticket_info['priority_icon_url']
        self.ticket_status = ticket_info['ticket_status']
        self.ticket_assignee_raw = ticket_info['ticket_assignee_raw']
        self.ticket_assignee = ticket_info['ticket_assignee']
        self.ticket_activity = ticket_info['ticket_activity']
        self.card_id = self.__generate_card_id()
        self.description = ticket_info['description']

    def __generate_card_id(self):
        card_id = binascii.hexlify(os.urandom(25))
        return card_id

    def build_card(self):

        self.card = {
        "style": "application",
        "url": "https://ww3.autotask.net/Autotask/Views/ServiceDesk/ServiceDeskTicket/service_ticket.aspx?ticketID={}".format(self.ticket_id),
        "format": "medium",
        "id": "{}".format(self.card_id),
        "title": "{}:{}".format(self.ticket_number, self.ticket_title),
        "description": "{}".format(self.description),
        "icon": {
            "url": "http://www.autotask.com/images/default-source/solutions/psa-logo-colored-icon.png?sfvrsn=2"
        },
        "attributes": [
            {
            "label": "Priority",
            "value": {
                "icon": {"url":"{}".format(self.priority_icon_url)},
                "label": "{}".format(self.ticket_priority)
            }
            },
            {
            "label": "Status",
            "value": {
                "label": "{}".format(self.ticket_status),
                "style": "lozenge-complete"
            }
            },
            {
            "label": "Assignee",
            "value": {
                "label": "{}".format(self.ticket_assignee),
                "url": "https://ww3.autotask.net/autotask35/grapevine/profile.aspx?resourceId={}".format(self.ticket_assignee_raw)
            }
            },
        ],
        "activity": {
            "html": self.ticket_activity
        }
        }

        return self.card
