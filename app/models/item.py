from rest_framework import serializers
from django import models

# Модель для "Предмета"
class Item(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField