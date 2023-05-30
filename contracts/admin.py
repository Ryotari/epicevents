from django.contrib import admin

from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Adds Contracts in the admin panel"""
    pass