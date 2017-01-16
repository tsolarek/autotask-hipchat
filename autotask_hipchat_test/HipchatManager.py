import re


class HipchatManager:
    def __init__(self, request):
        self.request = request
        self.message_text = self.get_message_text()
        self.message_sender = self.get_message_sender()
        self.room_id = self.request['item']['room']['id']
        self.message_id = self.request['item']['message']['id']
        self.contains_slash_command = self.check_contains_slash_command()
        self.contains_ticket_number = self.check_contains_ticket_number()

    def get_message_text(self):
        message_text = self.request['item']['message']['message']
        return message_text

    def get_message_sender(self):
        message_sender = self.request['item']['message']['from']['name']
        return message_sender

    def check_contains_slash_command(self):
        if self.message_text[0] == "/":
            return True
        else:
            return False

    def check_contains_ticket_number(self):
        pattern = r"T\d+.\d+.\d+"

        result = re.search(pattern, self.message_text)

        if result:
            return True
        else:
            return False

    def get_ticket_number(self):
        pattern = r"T\d+.\d+.\d+"

        result = re.findall(pattern, self.message_text)

        return result[0]
