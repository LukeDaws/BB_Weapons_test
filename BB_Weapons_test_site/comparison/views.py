from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def front_page(request):
    template = loader.get_template('front_page.html')
    return HttpResponse(template.render())


