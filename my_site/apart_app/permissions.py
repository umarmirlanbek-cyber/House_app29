from rest_framework.permissions import BasePermission

class BuyerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'buyer':
            return True
        return False

class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'