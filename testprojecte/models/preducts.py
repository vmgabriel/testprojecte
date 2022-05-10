"""Content Preducts"""

# Libraries
from django.db import models

 # Modules


class Preducts(models.Model):
    name = models.CharField("name", null=True, blank=True, max_length=120, )
    description = models.CharField("description", null=True, blank=True, max_length=120, )
    active = models.BooleanField("active", null=True, blank=True, )

    def __str__(self):
        return f"Preducts {self.pk}"

    def __repr__(self):
        return str(self)