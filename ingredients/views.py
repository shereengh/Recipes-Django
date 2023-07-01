from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import CategorySerializer,IngredientSerializer
from .models import Category,Ingredient

class CreateCategoryView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ListCategoryView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CreateIngredientView(CreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

class ListIngredientView(RetrieveAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "category"
    lookup_url_kwarg = "category_id"