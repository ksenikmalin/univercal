from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


menu = ['Меню 1', 'Меню 2', 'Меню 3']

def index(request):
    systems = System.objects.all()
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Мониторинг', 'active': True}],
        'title': 'Мониторинг',
        'menu': menu, 
        'systems': systems
    }
    return render(request, 'monitoring/index.html', context=context)

#def monitoring(request,pk):
#    if(pk == 0):
#        return redirect('home')
#        #raise Http404()
#    return HttpResponse(f"<h1>Страница приложения мониторинга Универсал!</h1><p>{pk}</p>")

def diagnostic(request):
    rooms = Room.objects.all()
    systems = System.objects.all()
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Диагностика', 'active': True}],
        'title': 'Диагностика',
        'menu': menu,
        'rooms':rooms,
        'systems':systems
    }
    return render(request, 'monitoring/diagnostic.html', context=context)

def statistics(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Статистика', 'active': True}],
        'title': 'Статистика',
        'menu': menu
    }
    return render(request, 'monitoring/statistics.html', context=context)

def customization(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Настройка', 'active': True}],
        'title': 'Настройка',
        'menu': menu
    }
    return render(request, 'monitoring/customization.html', context=context)

def help(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Помощь', 'active': True}],
        'title': 'Помощь',
        'menu': menu
    }
    return render(request, 'monitoring/help.html', context=context)

def reference(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Справка', 'active': True}],
        'title': 'Справка',
        'menu': menu
    }
    return render(request, 'monitoring/reference.html', context=context)

def contract(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Договор', 'active': True}],
        'title': 'Договор',
        'menu': menu
    }
    return render(request, 'monitoring/contract.html', context=context) 

def profile(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Профиль', 'active': True}],
        'title': 'Профиль',
        'menu': menu
    }
    return render(request, 'monitoring/profile.html', context=context) 

def register(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Регистрация', 'active': True}],
        'title': 'Регистрация',
        'menu': menu
    }
    return render(request, 'monitoring/register.html', context=context)

def login(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Авторизация', 'active': True}],
        'title': 'Авторизация',
        'menu': menu
    }
    return render(request, 'monitoring/login.html', context=context)

def errors(request):
    context = { 
        'history': [{'name' : 'Главная', 'active': False}, {'name': 'Ошибки', 'active': True}],
        'title': 'Ошибки',
        'menu': menu
    }
    return render(request, 'monitoring/errors.html', context=context)

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>Страница приложения Универсал не найдена!</h1>")