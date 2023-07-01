"""recipes_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userauth.views import UserCreateAPIView,UserLoginView
from ingredients.views import CreateCategoryView,ListCategoryView,CreateIngredientView,ListIngredientView
from recipes.views import CreateRecipeView,ListRecipeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',UserCreateAPIView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('category/add/',CreateCategoryView.as_view(),name='create-category'),
    path('category/',ListCategoryView.as_view(),name='category'),
    path('recipe/add/',CreateRecipeView.as_view(),name='create-recipe'),
    path('recipe/',ListRecipeView.as_view(),name='recipe'),
    path('ingredient/add/',CreateIngredientView.as_view(),name='create-ingredient'),
    path('ingredient/<int:category_id>/',ListIngredientView.as_view(),name='ingredient'),
]
