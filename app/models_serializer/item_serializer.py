from rest_framework import serializers
from ..models.item import Item

# Сериализация для "Предмета"
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id', 'name']