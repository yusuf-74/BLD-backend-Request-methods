from rest_framework.response import Response
from rest_framework import authentication , exceptions , permissions

class Authenticate(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get("authorization") == "ABCD":
            return (True , None)
        raise exceptions.AuthenticationFailed("not allowed")

class StudentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.headers.get("id") == '1':
            return True
        return False