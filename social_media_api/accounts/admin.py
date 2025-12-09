from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    model = User
    # Show these fields in admin user list
    list_display = ('username', 'email', 'is_staff', 'is_active')

