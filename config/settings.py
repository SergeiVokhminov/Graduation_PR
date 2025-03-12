# Импорт необходимых библиотек
import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

# BASE_DIR - определяет корневую директорию проекта.
# BASE_DIR - этот параметр используется для построения абсолютных путей внутри проекта.
# Основная директория проекта.
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ, используемый для криптографических подписей. Необходимо держать его в секрете.
SECRET_KEY = os.getenv("SECRET_KEY")

# Включает или отключает режим отладки.
# Включен (True) только в процессе разработки. При разворачивании на сервере обязательно установить значение False.
DEBUG = True if os.getenv("DEBUG") == "True" else False

# Список разрешенных доменов (используется "*" для разрешения всех), которые могут обслуживаться приложением.
ALLOWED_HOSTS = []

# Содержит список всех приложений, активированных в проекте.
# После создания своих приложений, их необходимо прописать тут!
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "drf_yasg",
    "users",
    "tasktracker",
    "employees",
]

# Список промежуточного ПО, которое обрабатывает входящие запросы и выходящие ответы.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Указывает на модуль маршрутизации, который будет использоваться для маршрутизации URL-адресов в проекте.
# URL-конфигурация корневого уровня.
ROOT_URLCONF = "config.urls"

# Настройки шаблонизации.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Указывает путь к WSGI-приложению. Это точка входа вашего приложения для совместимости с WSGI-серверами.
# Настройки необходимы в основном для разворачивания на сервере.
WSGI_APPLICATION = "config.wsgi.application"

# Настройки базы данных (Database - PostgreSQL). Использовать можно и другие базы данных.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT", default="5432"),
    }
}

# Список валидаторов, используемых для проверки надежности паролей пользователей.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Устанавливает язык для проекта.
LANGUAGE_CODE = "ru-ru"

# Устанавливает часовую зону для проекта.
TIME_ZONE = "Europe/Moscow"

# Включает поддержку интернационализации.
USE_I18N = True

# Включает поддержку локализации, применяя форматирование даты и времени.
USE_L10N = True

# Включает поддержку временных зон.
USE_TZ = True

# Настройки статических файлов.
# Содержит информацию о URL для доступа к статическим файлам.
STATIC_URL = "static/"
# Список директорий на диске, из которых будут подгружаться статические файлы.
# STATICFILES_DIRS = [BASE_DIR / "static"]

# Настройки медиатеки.
# Содержит информацию о URL для доступа к медиафайлам
MEDIA_URL = "/media/"
# Директория на диске, где будут храниться медиафайлы, загружаемые пользователем.
MEDIA_ROOT = BASE_DIR / "media"

# Определяет тип поля по умолчанию для первичных ключей всех приложений
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Стандартная модель пользователя
AUTH_USER_MODEL = "users.User"

# Именованный адрес на который следует перенаправлять пользователя после успешной авторизации
LOGIN_REDIRECT_URL = "/"
# Именованный адрес на который перенаправляется пользователь после выхода
LOGOUT_REDIRECT_URL = "/"

# Настройки для REST_FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Настройки срока действия токенов
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
