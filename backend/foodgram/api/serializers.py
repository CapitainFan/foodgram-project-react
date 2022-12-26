from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from recipe.models import Recipe
from users.models import User

RESTRICTED_USERNAME = 'me'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'login',
            'password',
            'email',
            'first_name',
            'last_name',
        )


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
