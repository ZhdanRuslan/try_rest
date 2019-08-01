from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'description', 'amount_items', 'child', 'amount_inner_categories')


class ItemListSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = models.Item
        fields = ('id', 'name', 'description', 'category', 'price')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
