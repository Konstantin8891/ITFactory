# ITFactory

## Описание

API для заполнения визитов в торговые точки

## Стек

Python 3.11

Django 4.2

PostgreSQL 15

Docker

Ожидается, что Python и Docker предустановлены на ПК.

## Переменные окружение

Ожидается, что в корне проекта есть .env файл следующего содержания (пример):

SECRET_KEY=django-insecure-ouq3n59t(mdj^rs+zde7+*ajjy47qp@ab=^jf%ngwcm+i_wwdu

DB_ENGINE=django.db.backends.postgresql 

DB_NAME=postgres 

POSTGRES_USER=postgres 

POSTGRES_PASSWORD=postgres 

DB_HOST=localhost

DB_PORT=5440

## Инструкция по запуску

git clone https://github.com/Konstantin8891/ITFactory.git

cd ITFactory

python3 -m venv venv

source venv/bin/activate (для Windows source venv/Scripts/activate)

cd infra_visit

docker-compose up 

cd ..

cd visit

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

## Примеры запросов

Добавить пользователя

POST api/add_user/ 

{"name":"Konstantin Vasilyev","phone":"+79217821766"}

Ответ

{"name":"Konstantin Vasilyev","phone":"+79217821766"}

Добавить торговую точку и прикрепить к нему сотрудника

POST api/add_shop/

{"name": "shawarma2", "phone": "+79217821766"}

Ответ

{"name": "shawarma2", "phone": "+79217821766"}

Получить список торговых точек, к которым привязан сотрудник

POST api/get_shops/

{"phone":"+79217821766"}

Ответ

[

    {
    
        "pk": 1,
        
        "name": "shawarma2"
        
    }
    
]

Оформить посещение 

POST api/visit_shop/

{

    "shop": 3,
    
    "phone": "+79217821766",
    
    "longitude": 35.5,
    
    "latitude": 35.5
    
}

Ответ

{

    "pk": 4,
    
    "date": "2023-10-12T13:32:44.199845Z"
    
}
