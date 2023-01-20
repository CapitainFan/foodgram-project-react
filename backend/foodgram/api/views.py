from datetime import datetime as dt

from django.contrib.auth import get_user_model
from django.db.models import F, Sum
from django.http.response import HttpResponse
from djoser.views import UserViewSet as DjoserUserViewSet
from foodgram.config import ACTION_METHODS, DATE_TIME_FORMAT
from recipes.models import AmountIngredient, Ingredient, Recipe, Tag
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .filters import AuthorAndTagFilter, IngredientFilter
from .mixins import AddDelViewMixin
from .paginators import PageLimitPagination
from .permissions import AdminOrReadOnly, AuthorStaffOrReadOnly
from .serializers import (IngredientSerializer, RecipeSerializer,
                          ShortRecipeSerializer, TagSerializer,
                          UserSubscribeSerializer)

User = get_user_model()


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AdminOrReadOnly,)


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = IngredientFilter
    search_fields = ('^name',)


class UserViewSet(DjoserUserViewSet, AddDelViewMixin):
    pagination_class = PageLimitPagination
    add_serializer = UserSubscribeSerializer

    @action(methods=ACTION_METHODS, detail=True,)
    def subscribe(self, request, id):
        return self.add_del_obj(id, 'subscribe')

    @action(methods=('get',), detail=False)
    def subscriptions(self, request):
        user = self.request.user
        if user.is_anonymous:
            return Response(status=HTTP_401_UNAUTHORIZED)
        authors = user.subscribe.all()
        pages = self.paginate_queryset(authors)
        serializer = UserSubscribeSerializer(
            pages, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)


class RecipeViewSet(ModelViewSet, AddDelViewMixin):
    queryset = Recipe.objects.all()
    serialier_class = RecipeSerializer
    permission_classes = (AuthorStaffOrReadOnly,)
    pagination_class = PageLimitPagination
    add_serializer = ShortRecipeSerializer
    filter_class = AuthorAndTagFilter

    @action(methods=ACTION_METHODS, detail=True,)
    def favorite(self, request, pk):
        return self.add_del_obj(pk, 'favorite')

    @action(methods=ACTION_METHODS, detail=True,)
    def shopping_cart(self, request, pk):
        return self.add_del_obj(pk, 'shopping_cart')

    @action(methods=('get',), detail=False)
    def download_shopping_cart(self, request):
        user = self.request.user
        if not user.carts.exists():
            return Response(status=HTTP_400_BAD_REQUEST)
        ingredients = AmountIngredient.objects.filter(
            recipe__in=(user.carts.values('id'))
        ).values(
            ingredient=F('ingredients__name'),
            measure=F('ingredients__measurement_unit')
        ).annotate(amount=Sum('amount'))

        filename = f'{user.username}_shopping_list.txt'
        shopping_list = (
            f'Список покупок для:\n\n{user.first_name}\n\n'
            f'{dt.now().strftime(DATE_TIME_FORMAT)}\n\n'
        )
        for ing in ingredients:
            shopping_list += (
                f'{ing["ingredient"]}: {ing["amount"]} {ing["measure"]}\n'
            )

        shopping_list += '\n\nПосчитано в Foodgram'

        response = HttpResponse(
            shopping_list, content_type='text.txt; charset=utf-8'
        )
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
