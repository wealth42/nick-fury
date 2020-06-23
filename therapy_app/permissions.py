from rest_framework.permissions import BasePermission


class NotAuthenticated(BasePermission):
    """
    Permission class which will be checking if the request not authenticated. (will be used for login function)
    """

    def has_permission(self, request, view):
        """This method will be called to evaluate if user has permission to access the api"""
        return not request.user.is_authenticated


class IsClient(BasePermission):
    """
    Permission class which will be checking if the request is done by Client or not.
    """

    def has_permission(self, request, view):
        """This method will be called to evaluate if user has permission to access the api"""
        return request.user.is_authenticated and request.user.type == "Client"


class IsTherapist(BasePermission):
    """
    Permission class which will be checking if the request is done by Therapist or not.
    """

    def has_permission(self, request, view):
        """This method will be called to evaluate if user has permission to access the api"""
        return request.user.is_authenticated and request.user.type == "Therapist"
