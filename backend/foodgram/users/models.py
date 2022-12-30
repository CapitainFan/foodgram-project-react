from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField, CheckConstraint, Q,
    ManyToManyField, EmailField,
)
from django.db.models.functions import Length
from django.utils.translation import gettext_lazy as _

CharField.register_lookup(Length)


class User(AbstractUser):
    email = EmailField(
        verbose_name='Электронная почта',
        unique=True,
    )
    username = CharField(
        verbose_name='Логин',
        max_length=69,
        unique=True,
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=69,
    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=69,
    )
    password = CharField(
        verbose_name=_('Пароль'),
        max_length=69,
    )
    subscribe = ManyToManyField(
        verbose_name='Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return f'{self.username}: {self.email}'
