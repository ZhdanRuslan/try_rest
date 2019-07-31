from django.db.models import Count
from rest_framework import generics

from . import models
from . import serializers


class CateListView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ItemListView(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()

    serializer_class = serializers.ItemSerializer
