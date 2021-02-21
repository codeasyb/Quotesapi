from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    
    """
        This is providing permissions if the user is admin or not
    """
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin
    