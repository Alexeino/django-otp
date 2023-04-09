from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('phone_number','is_phone_verified',)

admin.site.register(User)