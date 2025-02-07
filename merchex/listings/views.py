from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def view(request):
    return HttpResponse('<h1>A propos</h1> Nous adorons Merch')

def about(request):
    return HttpResponse('A propos')

def listings(request):
    return HttpResponse('<h1>liste des articles</h1> ')


def contacts(request):
    return HttpResponse('<h1>Nous contacter!</h1> ')