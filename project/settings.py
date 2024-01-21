from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/es/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "spacetour-relecloud.azurewebsites.net",
    ".azurewebsites.net",
    "127.0.0.1",
]

# Configuración de orígenes confiables para CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://spacetour-relecloud.azurewebsites.net",
    "http://spacetour-relecloud.azurewebsites.net",
    "https://.azurewebsites.net",
    "http://.azurewebsites.net",
    "http://127.0.0.1",
    "https://127.0.0.1",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "relecloud.apps.RelecloudConfig",
    "crispy_bootstrap4",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

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

WSGI_APPLICATION = "project.wsgi.application"

# Database
# https://docs.djangoproject.com/es/5.0/ref/settings/#databases

# Imprimo la contraseña de la base de datos
# print("0. Contraseña de la base de datos: ", os.environ.get("DATABASE_PASSWORD"))
# print("1. Contraseña de la base de datos: ", os.getenv("DATABASE_PASSWORD"))

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        # "HOST": "127.0.0.1",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "administrador1",
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": "relecloud.postgres.database.azure.com",
        "PORT": "5432",
        "OPTIONS": {"sslmode": "require"},  # SSL es para Azure
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/es/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/es/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/es/5.0/howto/static-files/

# Archivos estáticos (que no cambian: CSS, JavaScript, imágenes)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# Agrega la ruta completa de tus imágenes al final de STATICFILES_DIRS
STATICFILES_DIRS = [
    BASE_DIR / "relecloud" / "static",
    BASE_DIR / "relecloud" / "static" / "res" / "img" / "cruceros",
]

# Whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Archivos multimedia
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Configuración de correo electrónico
EMAIL_HOST = 'smtp.gmail.com'  # Aquí va la dirección del servidor SMTP
EMAIL_PORT = 587  # También puede ser 465, 25, 587
EMAIL_USE_TLS = True  # Muchos servidores SMTP requieren TLS
# EMAIL_USE_SSL = True  # Muchos servidores SMTP requieren SSL
EMAIL_HOST_USER = 'relecloudd@gmail.com'  # Tu dirección de correo electrónico
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Tu contraseña de correo electrónico