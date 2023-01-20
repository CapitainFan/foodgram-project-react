# Foodgram


### Описание
Это проект - продуктовый помошник, по курсу яндекс-практикум, в котором пользователь может зарегестрироваться, писать свои рецепты и прекрипить к ним теги, читать чужие, может составить список избранных рецептов и список продуктов.


### Технологии
- Python 3.7  - https://docs.python.org/release/3.7.0/

- Django 2.2.19 - https://docs.djangoproject.com/en/4.1/

- API - https://docs.python.org/release/3.7.0/distutils/apiref.html?highlight=api

- DRF - https://www.django-rest-framework.org/

- Nginx - https://nginx.org/en/docs/

- Docker - https://docs.docker.com/

- Gunicorn - https://docs.gunicorn.org/


### Как установить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:CapitainFan/foodgram-project-react.git
```


### Как запустить проект:

Переходим в нужную дерикторию:
```
cd foodgram-project-react
```

Поднимаем контейнеры :
```
docker-compose up -d --build
```

Выполняем миграции:

```
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Србираем статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```

Создаем резервную копию:
```
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json
```


### Останостановить контейнеры:
```
docker-compose down -v
```


### Примеры запросов

В проекте доступны следующие эндпоинты:

- Список пользователей
```
http://localhost/api/users/
```

- Профиль пользователя
```
http://localhost/api/users/{id}/
```

- Текущий пользователь
```
http://localhost/api/users/me/
```

- Изменение пароля
```
http://localhost/api/users/set_password/
```

- Получить токен авторизации
```
http://localhost/api/auth/token/login/
```

- Удаление токена
```
http://localhost/api/auth/token/logout/
```

- Cписок тегов / Получение тега
```
http://localhost/api/tags/{id}/
```

- Список рецептов / Создание рецепта
```
http://localhost/api/recipes/
```

- Получение рецепта / Обновление рецепта / Удаление рецепта
```
http://localhost/api/recipes/{id}/
```

- Скачать список покупок
```
http://localhost/api/recipes/download_shopping_cart/
```

- Добавить рецепт в список покупок / Удалить рецепт из списка покупок 
```
http://localhost/api/recipes/{id}/shopping_cart/
```

- Добавить рецепт в избранное / Удалить рецепт из избранного
```
http://localhost/api/recipes/{id}/favorite/
```

- Мои подписки. Возвращает пользователей, на которых подписан текущий пользователь. В выдачу добавляются рецепты.

```
http://localhost/api/users/subscriptions/
```

- Подписаться на пользователя / Отписаться от пользователя 
```
http://localhost/api/users/{id}/subscribe/
```

- Список ингредиентов 
```
http://localhost/api/ingredients/
```

- Получение ингредиента
```
http://localhost/api/ingredients/{id}/
```


### Авторы
Богдан Сокольников.