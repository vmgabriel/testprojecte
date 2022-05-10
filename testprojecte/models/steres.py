"""Content Steres"""

# Libraries
from django.db import models

 # Modules
from . import preducts


class Steres(models.Model):
    name = models.CharField("name", null=True, blank=True, max_length=120, )
    description = models.CharField("description", null=True, blank=True, max_length=120, )
    address = models.CharField("address", null=True, blank=True, max_length=120, )
    active = models.BooleanField("active", null=True, blank=True, )
    preducts_sc = models.ForeignKey(preducts.Preducts, on_delete=models.CASCADE)

    def __str__(self):
        return f"Steres {self.pk}"

    def __repr__(self):
        return str(self)