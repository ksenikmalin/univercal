1. Установка виртуального окружения

sudo apt-get install python3.8-venv
python3 -m venv venv

2. Активация виртуальной среды

source venv/bin/activate

3. Установка пакета django 

pip install django

4. Создание проекта app

django-admin startproject universal 

5. Миграция базы данных

python manage.py migrate

6. Запуск сервера

python manage.py runserver

7. Создание приложения

python manage.py startapp monitoring

8. Добавляем данные по моделям

Пишем в файле models.py

9. Создаем новые файлы миграции

python manage.py makemigrations

10. Добавляем новую миграцию в БД

python manage.py migrate

11. Добавление моделей в административную панель, действия производятся в admin.py

from .models import User
# Register your models here.

admin.site.register(User)

12. Создание суперпользователя для входа в админку

python manage.py createsuperuser

13. Вводим данные пользователя

Логин:user_test
Почта:user_test@mail.ru
Пароль:12345678

14. Переходим по адресу /admin 

15. Изменяем язык отображения данных в административной панели, в файле settings.py изменяем на

LANGUAGE_CODE = 'ru'       

16.Проблема миграции данных

python manage.py migrate --run-syncdb        

