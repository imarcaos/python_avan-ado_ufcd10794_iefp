from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
# View para devolver uma resposta http
def dizer_ola(request):
    return HttpResponse('<h1 style="color: blue">Olá eu sou a primeira aplicação em Django')