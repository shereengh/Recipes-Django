from rest_framework import serializers
from .models import Recipe,RecipeIngredient
from ingredients.models import Ingredient

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), write_only=True)
    quantity = serializers.CharField()
    class Meta:
        model = RecipeIngredient
        fields = ["quantity","ingredient"]

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ["title","author","ingredients"]
    
    def create(self,validated_data):
        ingredients = validated_data.pop("ingredients")
        print("ingredients: ",ingredients)
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            RecipeIngredient.objects.create(recipe=recipe,**ingredient)
        return recipe
