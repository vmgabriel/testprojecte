"""Content Sheppingcart"""

# Libraries
from django.db import models

 # Modules
from . import user
from . import preducts


class Sheppingcart(models.Model):
    ree_mame = models.CharField("ree_mame", null=True, blank=True, max_length=120, )
    user_sc = models.ForeignKey(user.User, on_delete=models.CASCADE)
    preducts_sc = models.ForeignKey(preducts.Preducts, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sheppingcart {self.pk}"

    def __repr__(self):
        return str(self)