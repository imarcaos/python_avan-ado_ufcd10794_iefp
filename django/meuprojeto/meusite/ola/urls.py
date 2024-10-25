from django.contrib import admin
from django.urls import path
from .views import dizer_ola

# Urls da aplicação (rotas)
urlpatterns = [
    path('ola', dizer_ola, name = 'ola') # define-me o caminho url para responder o ola
]