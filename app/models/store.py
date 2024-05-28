from rest_framework import serializers
from django import models
from item import Item

# Модель для "Хранилища"
class Store(models.Model):
    store_id = models.PositiveIntegerField(primary_key=True)
    report = models.ArrayField(
        model_container=Item,
    )