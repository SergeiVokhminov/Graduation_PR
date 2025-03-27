# Дипломный проект TB5.
Трекер задач сотрудников.

## Описание проекта.
Серверное приложение на Django и DRF для работы с базой данных PostgreSQL, представляющее собой трекер задач сотрудников. 
Приложение обеспечивает CRUD операции для сотрудников и задач, а также предоставляет два специальных эндпоинта 
для получения информации о загруженности сотрудников и важных задачах.
Трекер задач позволяет компании эффективно управлять заданиями, назначенными сотрудникам, 
и обеспечивать прозрачность процессов выполнения задач. 
Это поможет в равномерном распределении нагрузки между сотрудниками и своевременном выполнении ключевых задач.

## Папки, пакеты, приложения, шаблоны реализованные в проекте.
1. пакет config - основные настройки проекта;
2. директория media - содержит загруженные медиа файлы;
3. директорию fixture - содержит фикстуры сотрудников и задач;
4. приложения: employees, tasktracker, users.

## Используемые зависимости:
- amqp==5.3.1
- asgiref==3.8.1
- asttokens==3.0.0
- billiard==4.2.1
- black==24.10.0
- celery==5.4.0
- certifi==2024.12.14
- charset-normalizer==3.4.1
- class-registry==2.1.2
- click==8.1.8
- click-didyoumean==0.3.1
- click-plugins==1.1.1
- click-repl==0.3.0
- colorama==0.4.6
- coverage==7.6.10
- cron-descriptor==1.4.5
- decorator==5.1.1
- Django==5.1.4
- django-celery-beat==2.7.0
- django-cors-headers==4.6.0
- django-filter==24.3
- django-timezone-field==7.1
- djangorestframework==3.15.2
- djangorestframework_simplejwt==5.4.0
- drf-yasg==1.21.8
- executing==2.1.0
- filters==1.3.2
- flake8==7.1.1
- idna==3.10
- inflection==0.5.1
- ipython==8.31.0
- isort==5.13.2
- jedi==0.19.2
- kombu==5.4.2
- matplotlib-inline==0.1.7
- mccabe==0.7.0
- mypy==1.14.1
- mypy-extensions==1.0.0
- packaging==24.2
- parso==0.8.4
- pathspec==0.12.1
- pexpect==4.9.0
- pillow==11.1.0
- platformdirs==4.3.6
- prompt_toolkit==3.0.48
- psycopg2-binary==2.9.10
- ptyprocess==0.7.0
- pure_eval==0.2.3
- pycodestyle==2.12.1
- pyflakes==3.2.0
- Pygments==2.19.1
- PyJWT==2.10.1
- python-crontab==3.2.0
- python-dateutil==2.9.0.post0
- python-dotenv==1.0.1
- pytz==2024.2
- PyYAML==6.0.2
- redis==5.2.1
- regex==2024.11.6
- requests==2.32.3
- setuptools==75.5.0
- six==1.17.0
- sqlparse==0.5.3
- stack-data==0.6.3
- stripe==11.5.0
- traitlets==5.14.3
- typing_extensions==4.12.2
- tzdata==2025.1
- uritemplate==4.1.1
- urllib3==2.3.0
- vine==5.1.0
- wcwidth==0.2.13

## Установка:

1. Установите Git и Docker;
2. Клонируйте репозиторий:
'''
git clone https://github.com/SergeiVokhminov/Graduation_PR.git
'''
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Создайте и заполнить файл .env своими данными.

## Тестирование:
1. Для запуска подсчета покрытия тестами необходимо выполнить команду:
```
coverage run --source='.' manage.py test 
```
2. Чтобы вывести отчет по покрытию тестами, выполните команду:
```
coverage report
```
3. Покрытие тестами составляет 81%

## Запуск проекта:

1. Откройте терминал
2. Запустите команды:
  - "docker-compose build" - сборка образа проекта. 
  - "docker-compose up" - запуск образа проекта.
  - или сразу "docker-compose up -d --build" - сборка и запуск образа проекта.

## Проверка работоспособности проекта:
Сотрудник (Employees):
1. http://127.0.0.1:8000/employees/create/ - Создание сотрудника,
2. http://127.0.0.1:8000/employees/list/ - Просмотр списка сотрудников,
3. http://127.0.0.1:8000/employees/detail/{id}/ - Просмотр подробной информации о сотруднике,
4. http://127.0.0.1:8000/employees/update/{id}/ - Редактирование информации о сотруднике,
5. http://127.0.0.1:8000/employees/delete/{id}/ - Удаление сотрудника,
6. http://127.0.0.1:8000/employees/busy_employees/ - Просмотр информации о менее загруженном сотруднике.

Задача (Tasktracker):
1. http://127.0.0.1:8000/tasktracker/create/ - Создание задачи,
2. http://127.0.0.1:8000/tasktracker/list/ - Просмотр листа задач,
3. http://127.0.0.1:8000/tasktracker/detail/{id}/ - Просмотр подробной информации о задаче,
4. http://127.0.0.1:8000/tasktracker/update/{id}/ - Редактирование информации о задаче,
5. http://127.0.0.1:8000/tasktracker/delete/{id}/ - Удаление задачи,
6. http://127.0.0.1:8000/tasktracker/important/ - Просмотр информации о свободной задаче и кто ее может взять в работу.

API Документация:
1. http://127.0.0.1:8000/swagger/ - swagger API документация проекта,
2. http://127.0.0.1:8000/redoc/ - redoc API документация проекта.

## Документация

Для получения дополнительной информации обратитесь к [документации](README.md)
