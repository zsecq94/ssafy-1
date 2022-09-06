import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    family = ['mmm', 'QQQ', 'OOO']
    name = ['Alice']
    age = [25]
    context = {
        'family': family,
        'name': name,
        'age': age,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['가지덮밥', '차돌된장찌개', '오리주물럭', '열무국수']
    context = {
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # # raise
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.GET.get('message'))

    message = request.GET.get('message')
    mes = request.GET.get('mes1')
    context = {
        'message': message,
        'mes': mes,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'hello.html', context)