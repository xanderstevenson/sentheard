from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name', 'has_paid')
    list_filter = ('email', 'is_staff', 'is_active', 'first_name', 'last_name', 'has_paid')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'has_paid')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active', 'first_name', 'last_name', 'has_paid')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']


admin.site.register(CustomUser, CustomUserAdmin)