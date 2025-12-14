from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

User = get_user_model()

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')

