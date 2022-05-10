"""All Urls of Testprojecte"""

# Libraries
from django.urls import path

# Views
from . import views


app_name = "testprojectes"
urlpatterns = [
    # Steres
    path(
        "steress/",
        views.ListSteresView.as_view(),
        name="steress",
    ),
    path(
        "steress/new/",
        views.SteresCreateView.as_view(),
        name="steres-new",
    ),
    path(
        "steress/<int:pk>/edit/",
        views.SteresUpdateView.as_view(),
        name="steres-edit",
    ),
    path(
        "steress/<int:pk>/delete/",
        views.delete_steres_view,
        name="steres-delete",
    ),

    # User
    path(
        "users/",
        views.ListUserView.as_view(),
        name="users",
    ),
    path(
        "users/new/",
        views.UserCreateView.as_view(),
        name="user-new",
    ),
    path(
        "users/<int:pk>/edit/",
        views.UserUpdateView.as_view(),
        name="user-edit",
    ),
    path(
        "users/<int:pk>/delete/",
        views.delete_user_view,
        name="user-delete",
    ),

    # Preducts
    path(
        "preductss/",
        views.ListPreductsView.as_view(),
        name="preductss",
    ),
    path(
        "preductss/new/",
        views.PreductsCreateView.as_view(),
        name="preducts-new",
    ),
    path(
        "preductss/<int:pk>/edit/",
        views.PreductsUpdateView.as_view(),
        name="preducts-edit",
    ),
    path(
        "preductss/<int:pk>/delete/",
        views.delete_preducts_view,
        name="preducts-delete",
    ),

    # sheppingCart
    path(
        "sheppingcarts/",
        views.ListSheppingcartView.as_view(),
        name="sheppingcarts",
    ),
    path(
        "sheppingcarts/new/",
        views.SheppingcartCreateView.as_view(),
        name="sheppingcart-new",
    ),
    path(
        "sheppingcarts/<int:pk>/edit/",
        views.SheppingcartUpdateView.as_view(),
        name="sheppingcart-edit",
    ),
    path(
        "sheppingcarts/<int:pk>/delete/",
        views.delete_sheppingcart_view,
        name="sheppingcart-delete",
    ),

]