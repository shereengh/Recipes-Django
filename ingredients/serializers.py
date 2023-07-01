from rest_framework import serializers
from .models import Category, Ingredient

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class IngredientSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Ingredient
        fields = ["name","category"]

