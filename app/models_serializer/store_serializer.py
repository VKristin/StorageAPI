from rest_framework import serializers
from ..models.item import Store
from item_serializer import ItemSerializer

# Сериализация для "Хранилища"
class StoreSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Store
        fields = ['store_id', 'items']