# Foodgram
![yamdb](https://github.com/CapitainFan/foodgram-project-react/actions/workflows/main.yml/badge.svg)

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

### Ссылка на мой проект
http://textyourrecipe.sytes.net/


### To deploy this project need the next actions:
- Download project with SSH
```
git clone git@github.com:CapitainFan/foodgram-project-react.git
```
- Connect to your server:
```
ssh <server user>@<server IP>
```
- Install Docker on your server
```
sudo apt install docker.io
```
- Install Docker Compose (for Linux)
```
sudo apt install docker-compose
```
- Create project directory (preferably in your home directory)
```
mkdir foodgram && cd foodgram/
```
- Create env-file:
```
touch .env
```
- Fill in the env-file like it:
```
DEBUG=False(True если тестовый вариант и надо отслеживать ошибки)
SECRET_KEY=<Your_some_long_string>
ALLOWED_HOSTS='localhost, 127.0.0.1, <Your_host>'
CSRF_TRUSTED_ORIGINS='http://localhost, http://127.0.0.1, http://<Your_host>'
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD=<Your_password>
DB_HOST='db'
DB_PORT=5432
```
- Copy files from 'infra/' (on your local machine) to your server

- Run docker-compose
```
sudo docker-compose up -d
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
