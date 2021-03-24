"""Djago_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shell import views,socket_test,upload,json
urlpatterns = [
    path('admin/shell/monitor/', views.check),
    path('admin/', admin.site.urls),
    path('index/',views.linux),
    path('socket/', socket_test.socket_server),
    path('socket_conn/',views.socket_conn),
    path('upload/',upload.upload),
    path('upload_file/',upload.upload_file),
    path('post/',views.post),
    path('check/',views.check),
    path('checkinout/',views.checkinout),
    path('json/',json.rejson),
]
