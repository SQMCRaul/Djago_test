# coding:utf-8
"""
Django settings for Djago_test project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import time
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ipyappgkdxlo6ew84b^_u@1p+z4_7&$5v5d)2%(5lh0_qh2k6#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
# WEBSOCKET_ACCEPT_ALL=True

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shell.apps.ShellConfig',
    'dwebsocket',
    # 'corsheaders',
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Djago_test.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Djago_test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'mydb',
        'USER':'root',
        'PASSWORD':'sanquan123*',
        'HOST':'10.10.12.92',
        'PORT':'3306',
        'TEST': {
            'CHARSET' : 'utf8',
            'COLLATION':'utf8_general_ci'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#simpleui配置
# SIMPLEUI_INDEX = '/'
# SIMPLEUI_HOME_INFO = False
# SIMPLEUI_ANALYSIS = False
# SIMPLEUI_DEFAULT_ICON = False


# SIMPLEUI_CONFIG={
#
#     'system_keep':True,
#     'menus':[
#
#         {'name': 'Simpleui',
#         'icon': 'fas fa-code',
#         'url': 'http://10.10.12.94/monitor.html',
#          'codename':'monitor'
#          },
#         {
#         # 自2021.02.01+ 支持多级菜单，models 为子菜单名
#         'name': '多级菜单测试',
#         'icon': 'fa fa-file',
#
#       	# 二级菜单
#         'models': [
#             {
#             'name':'可视化',
#             'url':'http://10.10.12.94/monitor.html' ,
#             'codename':'graph'
#
#              },
#             {
#             'name': 'Baidu',
#             'icon': 'far fa-surprise',
#             'url':'/admin/shell/campusfiled'
#             # 第三级菜单 ，
#
#         }, {
#             'name': '内网穿透',
#             'url': '/admin/shell/host/',
#             'icon': 'fab fa-github'
#         }
#         ]
#         }
#
#     ]
# }


# SIMPLEUI_CONFIG = {
#     'system_keep': True,
#     'menu_display': ['Simpleui', '测试', '权限认证', '动态菜单测试'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
#     'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    # 'menus': [{
    #     'name': 'Simpleui',
    #     'icon': 'fas fa-code',
    #     'url': 'https://gitee.com/tompeppa/simpleui'
    # }, {
    #     'app': 'auth',
    #     'name': '权限认证',
    #     'icon': 'fas fa-user-shield',
    #     'models': [{
    #         'name': '用户',
    #         'icon': 'fa fa-user',
    #         'url': 'auth/user/'
    #     }]
    # }, {
    #     # 自2021.02.01+ 支持多级菜单，models 为子菜单名
    #     'name': '多级菜单测试',
    #     'icon': 'fa fa-file',
    #   	# 二级菜单
    #     'models': [{
    #         'name': 'Baidu',
    #         'icon': 'far fa-surprise',
    #         # 第三级菜单 ，
    #
    #     }, {
    #         'name': '内网穿透',
    #         'url': 'https://www.wezoz.com',
    #         'icon': 'fab fa-github'
    #     }]
    # }
    # ]
# }