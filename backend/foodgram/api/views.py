from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import filters, generics, status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from recipe.models import Ingredient, Recipe, Tag
from users.models import User

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    permission_classes = 
    filter_backends = (filters.SearchFilter, )
    filterset_fields = ('username')
    search_fields = ('username', )
    lookup_field = 'username'


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
