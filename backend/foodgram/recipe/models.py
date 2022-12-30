from django.contrib.auth import get_user_model
from django.db.models.functions import Length
from django.db.models import (
    CASCADE, CharField, CheckConstraint,
    DateTimeField, ForeignKey, ImageField,
    ManyToManyField, Model, IntegerField,
    Q, TextField, UniqueConstraint
)

CharField.register_lookup(Length)

User = get_user_model()


class Tag(Model):
    name = CharField(
        verbose_name='Название',
        max_length=100,
        unique=True,
    )
    color = CharField(
        max_length=6,
        blank=True,
        null=True,
        default="#ffffff",
    )
    slug = CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name', )
        constraints = (
            CheckConstraint(
                check=Q(name__length__gt=0),
                name='\n%(app_label)s_%(class)s_name is empty\n',
            ),
            CheckConstraint(
                check=Q(color__length__gt=0),
                name='\n%(app_label)s_%(class)s_color is empty\n',
            ),
            CheckConstraint(
                check=Q(slug__length__gt=0),
                name='\n%(app_label)s_%(class)s_slug is empty\n',
            ),
        )

    def __str__(self) -> str:
        return f'{self.name} (цвет: {self.color})'


class Ingredient(Model):
    name = CharField(
        verbose_name='Название',
        max_length=256,
    )
    measurement_unit = CharField(
        verbose_name='Единицы измерения',
        max_length=256
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('name', )
        constraints = (
            UniqueConstraint(
                fields=(
                    'name',
                    'units'
                ),
                name='unique_for_ingredient'
            ),
            CheckConstraint(
                check=Q(name__length__gt=0),
                name='\n%(app_label)s_%(class)s_name is empty\n',
            ),
            CheckConstraint(
                check=Q(measurement_unit__length__gt=0),
                name='\n%(app_label)s_%(class)s_units is empty\n',
            ),
        )

    def __str__(self):
        return f'{self.name} {self.measurement_unit}'


class Recipe(Model):
    author = ForeignKey(
        verbose_name='Автор',
        related_name='recipes',
        to=User,
        on_delete=CASCADE,
    )
    name = CharField(
        verbose_name='Название',
        max_length=256,
    )
    image = ImageField(
        verbose_name='Картинка',
        upload_to='recipes_images/'
    )
    ingredients = ManyToManyField(
        verbose_name='Ингредиенты',
        related_name='recipes',
        to=Ingredient,
        through='recipes.AmountIngredient',
    )
    cooking_time = IntegerField(
        verbose_name='Время приготовления в минутах',
        default=0,
    )
    text = TextField(
        verbose_name='Описание',
        max_length=1000,
    )
    favorite = ManyToManyField(
        verbose_name='Понравившиеся рецепты',
        related_name='favorites',
        to=User,
    )
    tags = ManyToManyField(
        verbose_name='Тег',
        related_name='recipes',
        to='Tag',
    )
    pub_date = DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    cart = ManyToManyField(
        verbose_name='Список покупок',
        related_name='shopping_list',
        to=User,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', )
        constraints = (
            UniqueConstraint(
                fields=(
                    'name',
                    'author',
                ),
                name='unique_for_author'
            ),
            CheckConstraint(
                check=Q(name__length__gt=0),
                name='\n%(app_label)s_%(class)s_name is empty\n',
            ),
        )

    def __str__(self):
        return f'{self.name}. Автор: {self.author.username}'


class AmountIngredient(Model):
    recipe = ForeignKey(
        verbose_name='В каких рецептах',
        related_name='ingredient',
        to=Recipe,
        on_delete=CASCADE,
    )
    ingredients = ForeignKey(
        verbose_name='Связанные ингредиенты',
        related_name='recipe',
        to=Ingredient,
        on_delete=CASCADE,
    )
    amount = IntegerField(
        verbose_name='Количество',
        default=0,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Количество ингридиентов'
        ordering = ('recipe', )
        constraints = (
            UniqueConstraint(
                fields=(
                    'recipe',
                    'ingredients',
                ),
                name='\n%(app_label)s_%(class)s ingredient alredy added\n',
            ),
        )

    def __str__(self) -> str:
        return f'{self.amount} {self.ingredients}'
