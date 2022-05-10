"""Views of Testprojecte"""

# Libraries
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Core
from core.views import FilteredListView

# App Contents
from . import models, filters, forms


# Steres

class ListSteresView(LoginRequiredMixin, FilteredListView):
    template_name = "steres/list.html"
    filterset_class = filters.SteresFilter
    model = models.steres.Steres
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class SteresCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Steres"""
    form_class = forms.SteresForm
    success_url = reverse_lazy("testprojectes:steress")
    template_name = "steres/new.html"


class SteresUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Steres"""
    form_class = forms.SteresForm
    success_url = reverse_lazy("testprojectes:steress")
    template_name = "steres/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.steres.Steres, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_steres_view(request, pk):
    steres = get_object_or_404(models.steres.Steres, pk=pk)
    steres.delete()
    return redirect("testprojectes:steress")


# User

class ListUserView(LoginRequiredMixin, FilteredListView):
    template_name = "user/list.html"
    filterset_class = filters.UserFilter
    model = models.user.User
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View User"""
    form_class = forms.UserForm
    success_url = reverse_lazy("testprojectes:users")
    template_name = "user/new.html"


class UserUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View User"""
    form_class = forms.UserForm
    success_url = reverse_lazy("testprojectes:users")
    template_name = "user/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.user.User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_user_view(request, pk):
    user = get_object_or_404(models.user.User, pk=pk)
    user.delete()
    return redirect("testprojectes:users")


# Preducts

class ListPreductsView(LoginRequiredMixin, FilteredListView):
    template_name = "preducts/list.html"
    filterset_class = filters.PreductsFilter
    model = models.preducts.Preducts
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class PreductsCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Preducts"""
    form_class = forms.PreductsForm
    success_url = reverse_lazy("testprojectes:preductss")
    template_name = "preducts/new.html"


class PreductsUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Preducts"""
    form_class = forms.PreductsForm
    success_url = reverse_lazy("testprojectes:preductss")
    template_name = "preducts/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.preducts.Preducts, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_preducts_view(request, pk):
    preducts = get_object_or_404(models.preducts.Preducts, pk=pk)
    preducts.delete()
    return redirect("testprojectes:preductss")


# Sheppingcart

class ListSheppingcartView(LoginRequiredMixin, FilteredListView):
    template_name = "sheppingcart/list.html"
    filterset_class = filters.SheppingcartFilter
    model = models.sheppingcart.Sheppingcart
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class SheppingcartCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Sheppingcart"""
    form_class = forms.SheppingcartForm
    success_url = reverse_lazy("testprojectes:sheppingcarts")
    template_name = "sheppingcart/new.html"


class SheppingcartUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Sheppingcart"""
    form_class = forms.SheppingcartForm
    success_url = reverse_lazy("testprojectes:sheppingcarts")
    template_name = "sheppingcart/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.sheppingcart.Sheppingcart, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_sheppingcart_view(request, pk):
    sheppingcart = get_object_or_404(models.sheppingcart.Sheppingcart, pk=pk)
    sheppingcart.delete()
    return redirect("testprojectes:sheppingcarts")


