from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS

from . import models
from . import serializers


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserListView(generics.ListCreateAPIView):
    """
        List of users Read-only
    """
    permission_classes = [ReadOnly]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
