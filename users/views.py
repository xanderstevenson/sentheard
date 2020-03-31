from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib import auth
from django.shortcuts import render, redirect


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('payments')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = auth.authenticate(username=email, password=password)
        auth.login(self.request, new_user)
        return valid

