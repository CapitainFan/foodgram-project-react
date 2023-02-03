from django.shortcuts import get_object_or_404
from foodgram.config import ADD_GET_METHODS, DEL_METHODS
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)


class AddDelViewMixin:
    add_serializer = None

    def add_del_obj(self, obj_id, meneger):
        assert self.add_serializer is not None, (
            f'{self.__class__.__name__} should include '
            'an `add_serializer` attribute.'
        )

        user = self.request.user
        if user.is_anonymous:
            return Response(status=HTTP_401_UNAUTHORIZED)

        menegers = {
            'subscribe': user.subscribe,
            'favorite': user.favorites,
            'shopping_cart': user.carts,
        }
        meneger = menegers[meneger]

        obj = get_object_or_404(self.queryset, id=obj_id)
        serializer = self.add_serializer(
            obj, context={'request': self.request}
        )
        obj_exist = meneger.filter(id=obj_id).exists()

        if (self.request.method in ADD_GET_METHODS) and not obj_exist:
            meneger.add(obj)
            return Response(serializer.data, status=HTTP_201_CREATED)

        if (self.request.method in DEL_METHODS) and obj_exist:
            meneger.remove(obj)
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(status=HTTP_400_BAD_REQUEST)