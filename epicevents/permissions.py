from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "management_member":
            return True
        return False

class IsSales(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "sales_member":
            return True
        return False

class IsSupport(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "support_member":
            return True
        return False