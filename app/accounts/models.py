from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Models extra information about users that are not built into Django's default user model.

    Example of extra information can be google user id, facebook user id, etc.
    """

    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    custom_auth_id = models.TextField(blank=True)
    facebook_oauth_id = models.TextField(blank=True)
    google_oauth_id = models.TextField(blank=True)
    twitter_oauth_id = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
