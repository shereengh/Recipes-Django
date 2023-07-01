from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import RecipeSerializer
from .models import Recipe

class CreateRecipeView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class ListRecipeView(ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
