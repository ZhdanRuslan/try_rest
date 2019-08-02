import django_filters
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models import F

from . import models
from . import serializers


class Index(View):
    """
        Index view. It's simply main page for useful access
        to try API in "manual mode" via browser
    """

    def get(self, request):
        return render(request, 'shop/index.html')


class ReadOnly(BasePermission):
    """
        Instance for safe access to API
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CategoryListView(generics.ListCreateAPIView):
    """
        View for API to work with list of categories. If user is not
        authenticated you got read-only access
    """
    permission_classes = [ReadOnly | IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        queryset = models.Category.objects.all()
        for elem in queryset:
            elem.amount_inner_categories = elem.get_descendant_count()
            elem.save()
        return queryset


class ItemListView(generics.ListCreateAPIView):
    """
        View for API to work with list of items. If user is not
        authenticated you got read-only access
    """
    permission_classes = [ReadOnly | IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['owner', 'category', 'price', 'amount_views', 'published']


class ItemDetailView(generics.RetrieveAPIView):
    """
        View for API to work with item. If user is not
        authenticated you got read-only access
    """
    permission_classes = [ReadOnly | IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = (request.path_info).split('/')[-1]
        models.Item.objects.filter(pk=pk).update(amount_views=F('amount_views') + 1)
        return super().get(request, *args, **kwargs)

    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemDestroyView(generics.DestroyAPIView):
    """
        View for API to work delete item. Only for
        authenticated users
    """
    permission_classes = [IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemUpdateView(generics.UpdateAPIView):
    """
        View for API to work update item. Only for
        authenticated users
    """
    permission_classes = [IsAuthenticated]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
