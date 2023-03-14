"""password_generator_progect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"), # '' - это означает что мы обращаемся по адресу главной страницы.(127.0.0.1.8000) name="home" это если нам надо конкретно перейти на эту страницу.
    path('password', views.password, name="password"), # name - именованный параметр
    path('about', views.about, name='about'),
    # это имя нашего конкретного обработчика пути.
    # Но тогда в action в HTML форме мы должны обращаться немного по другому.
    # В action ставим одинарные кавычки в путь.
]
