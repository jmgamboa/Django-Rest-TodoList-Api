from rest_framework import permissions


class CustomPermissions(permissions.BasePermission):
    """
    Pemission for users to add only to lists they own
     - owner may PUT, POST, DELETE their own Items/List
     - nobody else can access
     """
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        elif obj.list_name.owner_id != request.user.id:
            return "Permission Not Granted"

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method =="GET":
            return True
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user