from rest_framework import serializers
from django.db import models

# Модель для предметов
class Item(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True)
    quantity = models.PositiveBigIntegerField