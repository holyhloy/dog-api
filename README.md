## API для управления данными о собаках и их породах

Этот проект представляет собой RESTful API для управления 
информацией о собаках и их породах. API позволяет создавать, 
получать, обновлять и удалять записи о собаках и породах, 
а также предоставляет дополнительные данные, такие как 
средний возраст собак по породам и количество собак каждой породы.
Приложение упаковано в Docker, отдельно сервис web - django приложение
и db - БД PostgreSQL.

## Содержание

• Требования

• Установка

• Запуск проекта

• Структура проекта

• Примеры использования API

## Требования

Для работы с проектом вам понадобятся:

• Python 3.8 или выше

• Django 5.2

• Django REST Framework 3.16.0

• PostgreSQL 17

• Docker (для контейнеризации)

## Установка
#### Все команды выполняются в bash

1. Клонируйте репозиторий:


    git clone https://github.com/holyhloy/dog-api.git
    cd dog-api
   

2. Создайте виртуальное окружение и активируйте его:

   
    python -m venv venv \
    source venv/bin/activate
   

3. Установите зависимости:

   
    pip install -r requirements.txt
   

4. Создайте и настройте .env файл на основе .env.example:\


    DB_NAME = your_name
    DB_HOST = localhost
    DB_PORT = 5432
    DB_USER = postgres
    DB_PASS = your_password
    
    DEBUG=1
    SECRET_KEY=your_secret_key
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

Важно: при запуске приложения в контейнере, переменной \
DB_HOST необходимо присвоить имя сервиса docker-compose - 'db'

5. Выполните миграции для создания таблиц базы данных:

   
    python manage.py migrate
   

6. Создайте суперпользователя для доступа к админ-панели:

   
    python manage.py createsuperuser user


## Запуск

Запустите сервер в терминале:

    # ./.env
    ...
    DB_HOST=localhost
    ...   
    
    # bash
    python manage.py runserver

Или в Docker-контейнере:

    # ./.env
    ...
    DB_HOST=db
    ...    
    
    # bash
    docker-compose up -d --build
    
Теперь API доступен по адресу http://127.0.0.1:8000/api/.


## Структура проекта

• api/models.py: Определение моделей Dog и Breed.

• api/serializers.py: Сериализаторы для преобразования моделей в JSON и обратно.

• api/views.py: Логика обработки запросов к API, реализованы ModelViewSet'ы.

• api/urls.py: Определение маршрутов для эндпоинтов API с использованием роутера.

• dogs_app/settings.py: Конфигурация проекта Django.


## Примеры использования API
   
### Модель Dog

1. Получить список всех собак (GET на /api/dogs/):

   Ответ будет включать информацию о среднем возрасте собак каждой породы.


2. Создать новую собаку (POST на /api/dogs/):

   Пример запроса:
   
    {\
        "name": "Buddy",\
        "age": 3,\
        "gender": "Male",\
        "color": "Brown",\
        "favorite_food": "Chicken",\
        "favorite_toy": "Ball"
        "breed": 1
    }
   
   
3. Получить информацию о конкретной собаке (GET на /api/dogs/<id>/):

   Ответ будет включать количество собак той же породы.


4. Обновить информацию о собаке (PUT на /api/dogs/<id>/):

   Пример запроса:
   
   {
        "name": "Buddy",
        "age": 4,
        "gender": "Male",
        "color": "Brown",
        "favorite_food": "Fish",
        "favorite_toy": "Frisbee"
        "breed": 2
   }
   

5. Удалить собаку (DELETE на /api/dogs/<id>/)


### Модель Breed

1. Получить список всех пород (GET на /api/breeds/):

   Ответ будет включать количество собак каждой породы.


2. Создать новую породу (POST на /api/breeds/):

   Пример запроса:
   
   {
       "name": "Labrador",
       "size": "Large",
       "friendliness": 5,
       "trainability": 4,
       "shedding_amount": 3,
       "exercise_needs": 4
   }


3. Получить информацию о конкретной породе (GET на /api/breeds/<id>/)


4. Обновить информацию о породе (PUT на /api/breeds/<id>/):

    Пример запроса:

   {
       "name": "Labrador",
       "size": "Large",
       "friendliness": 1,
       "trainability": 2,
       "shedding_amount": 3,
       "exercise_needs": 4
   }


5. Удалить породу (DELETE на /api/breeds/<id>/)


