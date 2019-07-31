from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

from . import models
from . import serializers


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CateListView(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ItemListView(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
