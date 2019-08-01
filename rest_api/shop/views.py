import django_filters
from django.shortcuts import redirect, render
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models import F

from . import models
from . import serializers


class Index(View):
    def get(self, request):
        return render(request, 'shop/index.html')


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

    def get(self, request, *args, **kwargs):
        pk = (request.path_info).split('/')[-1]
        models.Item.objects.filter(pk=pk).update(amount_views=F('amount_views') + 1)
        return super().get(request, *args, **kwargs)

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
