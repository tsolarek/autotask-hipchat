from django.shortcuts import render
from django.template import context, loader

from django.views import generic
from django. http import JsonResponse, HttpResponse
from capabilities_descriptor import capabilities

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from models import OauthCredentials

from InstallationFlowManager import InstallationFlowManager
from AutotaskManager import AutotaskManager
from CardFactory import CardFactory
from Messenger import Messenger
from HipchatManager import HipchatManager


class DialogTestView(generic.View):

    def get(self, request, *args, **kwargs):
        template = loader.get_template('autotask_hipchat_test/templates/dialog_content.html')
        return HttpResponse(template.render())


class CapabilitiesView(generic.View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(capabilities)


class HipchatWebhookView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print incoming_message
        hipchat_manager = HipchatManager(incoming_message)
        if hipchat_manager.check_contains_ticket_number():
            at_manager = AutotaskManager(at_request=hipchat_manager.get_ticket_number(), activity=None)
            ticket_info = at_manager.get_ticket_info()
            card_factory = CardFactory(ticket_info)
            card = card_factory.build_card()
            messenger = Messenger(card, roomId=hipchat_manager.room_id, attach_to=True, message_id=hipchat_manager.message_id)
            messenger.send_notification()
        return HttpResponse()


class InstallableView(generic.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print incoming_message
        credentials = InstallationFlowManager(incoming_message)
        credentials.delete_oauth_credentials()
        credentials.create_oauth_credentials()
        return HttpResponse()


# Recieves POST request when a Ticket is created in AutoTask.
class AutotaskTicketCreateView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        reason = "Created"
        incoming_message = request.POST
        at_manager = AutotaskManager(incoming_message['number'], reason)
        ticket_info = at_manager.get_ticket_info()
        card_factory = CardFactory(ticket_info)
        card = card_factory.build_card()
        rooms = OauthCredentials.objects.all()
        for room in rooms:
            roomId = room.roomId
            messenger = Messenger(card, roomId)
            messenger.send_notification()

        return HttpResponse()


# Recieves POST request when the status of a ticket is changed in AutoTask.
class AutotaskTicketStatusUpdateView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        reason = "Status Updated"
        incoming_message = request.POST
        at_manager = AutotaskManager(incoming_message['number'], reason)
        ticket_info = at_manager.get_ticket_info()
        card_factory = CardFactory(ticket_info)
        card = card_factory.build_card()
        rooms = OauthCredentials.objects.all()
        for room in rooms:
            roomId = room.roomId
            print roomId
            messenger = Messenger(card, roomId)
            messenger.send_notification()

        return HttpResponse()


class UninstalledView(generic.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print incoming_message
        return HttpResponse()
