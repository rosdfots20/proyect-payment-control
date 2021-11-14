import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2zn+_kj3!nbfo&3g5rqh&%!g2w0jgse0)f*-0)phv9s&)@*d@y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'pwa',
    'finance',
    'student',
    'pagos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'site_school.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'site_school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

PWA_APP_NAME = "Universidad"
PWA_APP_DESCRIPTION = "Universidad de los Angeles"
PWA_APP_THEME_COLOR = "#3477f5"
PWA_APP_BACKGROUND_COLOR = "#6699f7"
PWA_APP_ICONS = [
    {
        "src": "/static/core/img/icons/iconx72.png",
        "sizes": "72x72" 
    },
    {
        "src": "/static/core/img/icons/iconx96.png",
        "sizes": "96x96" 
    },
    {
        "src": "/static/core/img/icons/iconx128.png",
        "sizes": "128x128" 
    },
    {
        "src": "/static/core/img/icons/iconx144.png",
        "sizes": "144x144" 
    },
    {
        "src": "/static/core/img/icons/iconx152.png",
        "sizes": "152x152" 
    },
    {
        "src": "/static/core/img/icons/iconx192.png",
        "sizes": "192x192" 
    },
    {
        "src": "/static/core/img/icons/iconx384.png",
        "sizes": "384x384" 
    },
    {
        "src": "/static/core/img/icons/iconx512.png",
        "sizes": "512x512" 
    }
]

PWA_APP_ICONS_APPLE = [
    {
        "src": "/static/core/img/icons/iconx72.png",
        "sizes": "72x72" 
    },
    {
        "src": "/static/core/img/icons/iconx96.png",
        "sizes": "96x96" 
    },
    {
        "src": "/static/core/img/icons/iconx128.png",
        "sizes": "128x128" 
    },
    {
        "src": "/static/core/img/icons/iconx144.png",
        "sizes": "144x144" 
    },
    {
        "src": "/static/core/img/icons/iconx152.png",
        "sizes": "152x152" 
    },
    {
        "src": "/static/core/img/icons/iconx192.png",
        "sizes": "192x192" 
    },
    {
        "src": "/static/core/img/icons/iconx384.png",
        "sizes": "384x384" 
    },
    {
        "src": "/static/core/img/icons/iconx512.png",
        "sizes": "512x512" 
    }
]

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, "serviceworker.js")