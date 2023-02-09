from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Manages Permissions for users"""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Update status permission"""

    def has_object_permission(self, request, view, obj):
        """Check permission"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id