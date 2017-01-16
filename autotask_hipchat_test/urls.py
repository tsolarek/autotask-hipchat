from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^dialog/?$', views.DialogTestView.as_view(), name='dialog'),
    url(r'^capabilities/?$', views.CapabilitiesView.as_view(), name='capabilities'),
    url(r'^6e4bc5e465456a4fae109743b3c270e2c297ae6b43ce6df64a/?$', views.HipchatWebhookView.as_view(), name="hipchat_webhook"),
    url(r'^installable/?$', views.InstallableView.as_view(), name="installable"),
    url(r'^uninstalled/?$', views.UninstalledView.as_view(), name="uninstalled"),
    url(r'^0cbc56706d9de6dcffebfda1b5af9623279231d72eb5b7f9cc/?$', views.AutotaskTicketStatusUpdateView.as_view(), name="at_ticket_status_update"),
    url(r'^fba37ad940f62da03d645e20263e06a00f7351f6c58861d12d/?$', views.AutotaskTicketCreateView.as_view(), name="at_ticket_create"),
]