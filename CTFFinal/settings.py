"""
Django settings for CTF project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
from django.utils import timezone
from datetime import datetime, timedelta


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
	"constance",
	"app",
	"constance.backends.database",
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
]

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"whitenoise.middleware.WhiteNoiseMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "CTFFinal.urls"

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

WSGI_APPLICATION = "CTFFinal.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

MODE = 'development'

if MODE == 'development':
	DATABASES = {
		"default": {
			"ENGINE": "django.db.backends.sqlite3",
			"NAME": os.path.join(BASE_DIR, "db.sqlite3"),
		}
	}

elif MODE == 'production':
	DATABASES = {
		"default": dj_database_url.config(conn_max_age=500),

		"receipts": {
			"ENGINE": "django.db.backends.mysql",
			"NAME": os.environ.get("DB_NAME"),
			"HOST": os.environ.get("DB_HOST"),
			"PORT": 3306,
			"USER": os.environ.get("DB_USER"),
			"PASSWORD": os.environ.get("DB_PASSWORD"),
			"OPTIONS": {
				"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
			},
		},
	}

if MODE == 'development':
	CACHES = {

	    'default': {
	        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
	    }
	}
elif MODE == 'production':
	CACHES = {
    	
    	'default': {
        	'BACKEND': 'django_bmemcached.memcached.BMemcached',
        	'LOCATION': os.environ.get("MEMCACHIER_SERVERS"),
        	'OPTIONS':{
        		'username': os.environ.get("MEMCACHIER_USERNAME"),
        		'password': os.environ.get("MEMCACHIER_PASSWORD")
    		}
    	}
	}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		"NAME":
		"django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
	},
	{
		"NAME":
		"django.contrib.auth.password_validation.MinimumLengthValidator",
	},
	{
		"NAME":
		"django.contrib.auth.password_validation.CommonPasswordValidator",
	},
	{
		"NAME":
		"django.contrib.auth.password_validation.NumericPasswordValidator",
	},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "app.Team"

MEDIA_ROOT = os.path.join(BASE_DIR, "Uploads")

MEDIA_URL = "downloads/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

AUTH_USER_MODEL = "app.Team"

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
TIME_ZONE = 'Asia/Calcutta'
USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


CONSTANCE_CONFIG = {
    'START_TIME': (timezone.now(),'Start Time of the Event',datetime),
    'END_TIME': (timezone.now() + timedelta(minutes = 60),'End Time of the Event',datetime),
}
