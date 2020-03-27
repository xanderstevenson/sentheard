from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')