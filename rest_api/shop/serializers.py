from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for category
    """
    class Meta:
        model = models.Category
        fields = ('parent', 'name', 'amount_items', 'amount_inner_categories')


class ItemListSerializer(serializers.ModelSerializer):
    """
        Serializer for list of items
    """

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = models.Item
        fields = ('id', 'name', 'description', 'category', 'price', 'amount_views')


class ItemSerializer(serializers.ModelSerializer):
    """
        Serializer for one item
    """
    class Meta:
        model = models.Item
        fields = '__all__'
