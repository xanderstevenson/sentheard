from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class DeactivateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active']