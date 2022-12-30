from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from django.urls import reverse_lazy
from djoser.views import UserViewSet as DjoserUserViewSet
from django.views.generic import CreateView
from rest_framework import filters, generics, status, mixins
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from recipe.models import AmountIngredient, Ingredient, Recipe, Tag
from users.models import User

from .mixins import AddDelViewMixin
from .paginators import PageLimitPagination
from .permissions import AdminOrReadOnly, AuthorStaffOrReadOnly
from .serializers import (IngredientSerializer, RecipeSerializer,
                          ShortRecipeSerializer, TagSerializer,
                          UserSubscribeSerializer)


class UserViewSet(DjoserUserViewSet, AddDelViewMixin):
    pagination_class = PageLimitPagination
    add_serializer = UserSubscribeSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AdminOrReadOnly,)


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
