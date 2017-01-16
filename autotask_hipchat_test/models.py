from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class OauthCredentials(models.Model):
    oauthId = models.CharField(max_length=255)
    oauthSecret = models.CharField(max_length=255)
    roomId = models.CharField(max_length=255)
    groupId = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255, default="none")

    def __str__(self):
        return self.oauthId
