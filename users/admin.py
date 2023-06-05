from django.contrib import admin

from .models import Client, User

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Adds Clients in the admin panel"""
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Adds Users in the admin panel"""
    pass