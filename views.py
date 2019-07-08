# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView # 追記
from django.contrib.auth.forms import UserCreationForm  # 追記
from django.urls import reverse_lazy # 追記
# from django.views.generic import TemplateView
from . import forms

class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

class indexView(TemplateView):
    template_name = "accounts/index.html"

class createView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/create.html"
    success_url = reverse_lazy("login")