"""Forms of Testprojecte APP"""

# Libraries
from django import forms

# Models
from . import models

class SteresForm(forms.ModelForm):
    """Form to Steres"""
    preducts_sc = forms.ModelChoiceField(queryset=models.preducts.Preducts.objects.all())

    class Meta:
        model = models.steres.Steres
        fields = ["name", "description", "address", "active", "preducts_sc", ]


class UserForm(forms.ModelForm):
    """Form to User"""

    class Meta:
        model = models.user.User
        fields = ["name", "nick", ]


class PreductsForm(forms.ModelForm):
    """Form to Preducts"""

    class Meta:
        model = models.preducts.Preducts
        fields = ["name", "description", "active", ]


class SheppingcartForm(forms.ModelForm):
    """Form to Sheppingcart"""
    user_sc = forms.ModelChoiceField(queryset=models.user.User.objects.all())
    preducts_sc = forms.ModelChoiceField(queryset=models.preducts.Preducts.objects.all())

    class Meta:
        model = models.sheppingcart.Sheppingcart
        fields = ["ree_mame", "user_sc", "preducts_sc", ]


