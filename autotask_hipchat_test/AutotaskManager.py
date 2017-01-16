import atws


class AutotaskManager:
    def __init__(self, at_request, activity):
        self.__ticket_number = at_request
        print self.__ticket_number
        self.__at_username = 'removed'
        self.__at_password = 'removed'
        self.__at = atws.connect(username=self.__at_username, password=self.__at_password)
        self.__ticket = self.__get_at_ticket_details()
        self.__activity_raw = activity

        self.__ticket_title = self.__ticket.Title
        self.__ticket_id = self.__ticket.id
        self.__ticket_priority_raw = self.__ticket.Priority
        self.__ticket_priority = self.__get_priority()
        self.__ticket_status_raw = self.__ticket.Status
        self.__ticket_status = self.__get_status()
        self.__ticket_assignee_raw = self.__get_assginee_raw()
        self.__ticket_assignee = self.__get_assignee()

        self.__priority_icon_url = self.__get_priority_icon_url()
        self.__activity = self.__get_ticket_activity()
        self.__description = self.__get_description()

    def __get_at_ticket_details(self):
        query = atws.Query('Ticket')
        query.WHERE('TicketNumber', query.Equals, self.__ticket_number)
        result = self.__at.query(query).fetch_all()
        ticket = result[0]

        return ticket

    def get_ticket_info(self):

        ticket_info = {
            'ticket_number': '{}'.format(self.__ticket_number),
            'ticket_title': '{}'.format(self.__ticket_title),
            'ticket_id': '{}'.format(self.__ticket_id),
            'ticket_priority': '{}'.format(self.__ticket_priority),
            'priority_icon_url': '{}'.format(self.__priority_icon_url),
            'ticket_status': '{}'.format(self.__ticket_status),
            'ticket_assignee_raw': '{}'.format(self.__ticket_assignee_raw),
            'ticket_assignee': '{}'.format(self.__ticket_assignee),
            'ticket_activity': '{}'.format(self.__activity),
            'description': '{}'.format(self.__description),
        }

        return ticket_info

    def __get_priority(self):
        if self.__ticket_priority_raw == 1:
            return "High"
        elif self.__ticket_priority_raw == 2:
            return "Medium"
        elif self.__ticket_priority_raw == 3:
            return "Low"
        elif self.__ticket_priority_raw == 4:
            return "Critical"

    def __get_status(self):
        if self.__ticket_status_raw == 8:
            return "In Progress"
        elif self.__ticket_status_raw == 10:
            return "Dispatched"
        elif self.__ticket_status_raw == 5:
            return "Complete"
        elif self.__ticket_status_raw == 12:
            return "Waiting Vendor"
        elif self.__ticket_status_raw == 11:
            return "Escalate"
        elif self.__ticket_status_raw == 17:
            return "On Hold"
        elif self.__ticket_status_raw == 7:
            return "Waiting Customer"
        elif self.__ticket_status_raw == 15:
            return "Change Order"
        elif self.__ticket_status_raw == 19:
            return "Customer Note Added"
        elif self.__ticket_status_raw == 16:
            return "Inactive"
        elif self.__ticket_status_raw == 14:
            return "Billed"
        elif self.__ticket_status_raw == 1:
            return "New"
        elif self.__ticket_status_raw == 9:
            return "Waiting Materials"
        elif self.__ticket_status_raw == 13:
            return "Waiting Approval"
        elif self.__ticket_status_raw == 18:
            return "Ready to Bill"

    def __get_assignee(self):
        query = atws.Query('Resource')
        query.WHERE('id', query.Equals, self.__ticket_assignee_raw)
        result = self.__at.query(query).fetch_all()
        resource = result[0]
        full_name = str(resource.FirstName) + " " + str(resource.LastName)

        return full_name

    def __get_priority_icon_url(self):
        priority_icon_url = ""

        if self.__ticket_priority == "Low":
            priority_icon_url = "https://jira.atlassian.com/images/icons/priorities/trivial.svg"
        elif self.__ticket_priority == "Medium":
            priority_icon_url = "https://jira.atlassian.com/images/icons/priorities/minor.svg"
        elif self.__ticket_priority == "High":
            priority_icon_url = "https://jira.atlassian.com/images/icons/priorities/major.svg"
        elif self.__ticket_priority == "Critical":
            priority_icon_url = "https://jira.atlassian.com/images/icons/priorities/critical.svg"

        return priority_icon_url

    def __get_ticket_activity(self):
        if self.__activity_raw == 'Created':
            return "<b>{}</b>: {} <b>{}</b>".format(self.__ticket_number, self.__ticket_title, "created")
        elif self.__activity_raw == 'Status Updated':
            return "<b>{}</b>: {} <b>{}</b>".format(self.__ticket_number, self.__ticket_title, "status updated to {}".format(self.__ticket_status))
        else:
            return "<b>{}</b>: {}".format(self.__ticket_number, self.__ticket_title)

    def __get_description(self):
        try:
            description = str(self.__ticket.Description)
        except:
            description = " "

        return description

    def __get_assginee_raw(self):
        try:
            ticket_assignee_raw = self.__ticket.AssignedResourceID
        except AttributeError:
            ticket_assignee_raw = self.__ticket.CreatorResourceID

        return ticket_assignee_raw

