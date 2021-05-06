## Описание
Тестовое задание. Создание коротких адресов. Есть возможность внести в черный список адреса и домены через панель администратора.
База данных в контейнере docker.

Основные файлы:
- [views.py](https://github.com/fsowme/test_url_shortener/blob/master/url_shortener/shortener/views.py)
- [models.py](https://github.com/fsowme/test_url_shortener/blob/master/url_shortener/shortener/models.py)

## Запуск
```
git clone git@github.com:fsowme/test_url_shortener.git
cd test_url_shortener
python -m venv venv && source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
touch .env && nano .env
```

#### Пример наполнения .env
```
SECRET_KEY= "secret_key"
DB_ENGINE="django.db.backends.postgresql"
POSTGRES_DB="db"
DB_HOST="localhost"
DB_PORT="5432"
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
```

#### Что бы сгенерировать secret key можно использовать встроенную функцию django
```
python url_shortener/manage.py shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### запуск postgresql:
```
sudo docker-compose up -d
```

#### Подготовка django
```
cd url_shortener
python manage.py makemigrations shortener && python manage.py migrate
python manage.py createsuperuser
```

#### Запуск django
```
python manage.py runserver
```

#### При post запросе необходимо либо добавить X-CSRFToken в header, либо отключить проверку во views.py
```
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
```

#### Использованные технологии
- Django
- Docker
