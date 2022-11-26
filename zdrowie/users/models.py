from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages




class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
    bio = models.TextField(blank=True, null=True, max_length=500)


    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
