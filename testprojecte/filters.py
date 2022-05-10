"""Filter App Testprojecte"""

# Libraries
import django_filters

# Models
from . import models


class SteresFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Name", lookup_expr="icontains")
    description = django_filters.CharFilter(label="Description", lookup_expr="icontains")
    address = django_filters.CharFilter(label="Address", lookup_expr="icontains")
    active = django_filters.BooleanFilter(label="Active", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("name", "Name"),
            ("description", "Description"),
            ("address", "Address"),
            ("active", "Active"),
            ("preducts_sc", "Preducts_sc"),
        ),
    )

    class Meta:
        model = models.steres.Steres
        fields = ["name", "description", "address", "active", "preducts_sc", ]


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Name", lookup_expr="icontains")
    nick = django_filters.CharFilter(label="Nick", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("name", "Name"),
            ("nick", "Nick"),
        ),
    )

    class Meta:
        model = models.user.User
        fields = ["name", "nick", ]


class PreductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Name", lookup_expr="icontains")
    description = django_filters.CharFilter(label="Description", lookup_expr="icontains")
    active = django_filters.BooleanFilter(label="Active", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("name", "Name"),
            ("description", "Description"),
            ("active", "Active"),
        ),
    )

    class Meta:
        model = models.preducts.Preducts
        fields = ["name", "description", "active", ]


class SheppingcartFilter(django_filters.FilterSet):
    ree_mame = django_filters.CharFilter(label="Ree_mame", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("ree_mame", "Ree_mame"),
            ("user_sc", "User_sc"),
            ("preducts_sc", "Preducts_sc"),
        ),
    )

    class Meta:
        model = models.sheppingcart.Sheppingcart
        fields = ["ree_mame", "user_sc", "preducts_sc", ]


