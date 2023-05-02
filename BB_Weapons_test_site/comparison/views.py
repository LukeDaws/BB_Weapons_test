from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Weapons

def list(request):
    weapons_list = Weapons.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'weapons_list': weapons_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    weapons_list = Weapons.objects.get(slug = slug)
    template = loader.get_template('details.html')
    context = {
        'weapons_list': weapons_list,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    weapons_available = Weapons.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'weapons_available' : weapons_available,
    }
    return HttpResponse(template.render(context, request))