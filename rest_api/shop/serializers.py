from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'description', 'amount_items', 'parent', 'amount_inner_categories')


class ItemListSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = models.Item
        fields = ('id', 'name', 'description', 'category', 'price', 'amount_views')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = '__all__'
