from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

# def render(request: Any, - запрос
#            template_name: Any, - имя шаблона
#            context: Any = None, - передается переменная в виде ключа и значения
#            content_type: Any = None,
#            status: Any = None,
#            using: Any = None) -> HttpResponse

# Во Flask передается параметры как ключ значение то в django передается словарь с клчём и значением.
# Будем генерировать какие-та пароли. templates каталог будет браться путь по умолчанию, а generator путь нужно указать.
# context: Any = None третий параметр переменная которая включает в себя словарь в котором есть ключ и значение.
# этот ключ доступен на HTML страничке home по пути второго параметра.
def home(request) -> HttpResponse:
    """Функция, возвращает ответ HTML шаблон templates"""
    # Напишем длину пароля
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})

## Нам нужна еще одна страница, где будет отображаться наш пароль. ## Что бы обработчик сделал какую-то задачу, нам нужен URL.
def password(request) -> HttpResponse:
    """Функция, возвращает ответ HTML шаблон templates, возвращает сгенерированный пароль, свзянный с выпадающим списком."""
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get('length')) # GET - в виде аббревиатуры, get - метод получить Через get параметры, что бы передавались данные которые выбираются.
    psw = ''
    for _ in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw}) # password - на HTML странице могу обращаться по имени password, psw - имя переменной которую хотим вывести на HTML странице.

def about(request):
    return render(request, 'generator/about.html')