"""Content User"""

# Libraries
from django.db import models

 # Modules


class User(models.Model):
    name = models.CharField("name", null=True, blank=True, max_length=120, )
    nick = models.CharField("nick", null=True, blank=True, max_length=120, )

    def __str__(self):
        return f"User {self.pk}"

    def __repr__(self):
        return str(self)