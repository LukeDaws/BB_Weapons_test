from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('list/', views.list, name='list'),
    path('list/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]