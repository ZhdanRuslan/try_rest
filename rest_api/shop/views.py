import django_filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from . import models
from . import serializers


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CategoryListView(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class ItemListView(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['owner', 'category', 'price', 'amount_views', 'published']


class ItemDetailView(generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemDestroyView(generics.DestroyAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemUpdateView(generics.UpdateAPIView):
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
