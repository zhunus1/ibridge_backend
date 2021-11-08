from django.conf import settings

from rest_framework.permissions import BasePermission

class APIKeyPermission(BasePermission):
    def has_permission(self, request, view):
        api_key = request.META['HTTP_X_API_KEY']
        return api_key == settings.API_KEY_SECRET
