import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+mv^)6xk*-3jxga93jx6uku_zp1vdhz850co@bai3)c2$amy*v'

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

    # 자신이 생성한 app을 정의합니다.
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT URL을 정의합니다.
# 현재 project의 urls파일이기 때문에 url요청이 들어오면 해당 파일에 있는 url을 읽습니다.
ROOT_URLCONF = 'djangogirls.urls'

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

WSGI_APPLICATION = 'djangogirls.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# 데이터 베이스를 정의합니다.
# 현재 장고에서 기본적으로 제공해주는 sqlite3를 사용하고 있습니다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # 한글

TIME_ZONE = 'Asia/Seoul' # 서울 시간

USE_I18N = True # 국제화라는 의미, 다른 국가의 사람들에게도 읽힐 수 있게 만드는 작업

USE_L10N = True # 현지화라는 의미, 단순히 내용이 읽히는 것에 더해서 지역명이나 인물을 바꾸거나, 숙어와 속담, 문화와 생활 양식 등을 대상 국가에 맞춰 치환해서 현지화

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Staic 파일의 경로를 지정합니다.
STATIC_URL = '/static/'
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'blog/static'),
]
