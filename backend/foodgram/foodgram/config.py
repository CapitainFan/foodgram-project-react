from string import hexdigits

from recipe.models import AmountIngredient
from rest_framework.serializers import ValidationError


def recipe_amount_ingredients_set(recipe, ingredients):
    for ingredient in ingredients:
        AmountIngredient.objects.get_or_create(
            recipe=recipe,
            ingredients=ingredient['ingredient'],
            amount=ingredient['amount'],
        )


def is_hex_color(value):
    if len(value) not in (3, 6):
        raise ValidationError(
            f'{value} не правильной длины ({len(value)}).'
        )
    if not set(value).issubset(hexdigits):
        raise ValidationError(
            f'{value} не шестнадцатиричное.'
        )


def check_value_validate(value, klass=None):
    if not str(value).isdecimal():
        raise ValidationError(
            f'{value} должно содержать цифру'
        )
    if klass:
        obj = klass.objects.filter(id=value)
        if not obj:
            raise ValidationError(
                f'{value} не существует'
            )
        return obj[0]


RESTRICTED_USERNAME = 'me'

MIN_USERNAME_LEN = 3
MAX_USERNAME_LEN = 50

TRANSLATER_DICT = str.maketrans(
    'qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
    'йцукенгшщзхъфывапролджэячсмитьбю.'
)

ADD_METHODS = ('GET', 'POST',)
DEL_METHODS = ('DELETE',)
ACTION_METHODS = [s.lower() for s in (ADD_METHODS + DEL_METHODS)]
UPDATE_METHODS = ('PUT', 'PATCH')

SYMBOL_TRUE_SEARCH = ('1', 'true',)
SYMBOL_FALSE_SEARCH = ('0', 'false',)

LEN_HEX_COLOR = 6
MAX_LEN_EMAIL_FIELD = 254
MAX_LEN_RECIPES_CHARFIELD = 200
MAX_LEN_RECIPES_TEXTFIELD = 5000
MAX_LEN_USERS_CHARFIELD = 150

# help-text для email
USERS_HELP_EMAIL = (
    'Обязательно для заполнения. '
    f'Максимум {MAX_LEN_EMAIL_FIELD} букв.'
)
# help-text для username
USERS_HELP_UNAME = (
    'Обязательно для заполнения. '
    f'От {MIN_USERNAME_LEN} до {MAX_USERNAME_LEN} букв.'
)

# help-text для first_name/last_name
USERS_HELP_FNAME = (
    'Обязательно для заполнения.'
    f'Максимум {MAX_USERNAME_LEN} букв.'
)
