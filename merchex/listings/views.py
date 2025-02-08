from django.http import HttpResponse

from django.shortcuts import render
from listings.models import Band , Announce
# Create your views here.

def hello(request):
    bands= Band.objects.all()
    return HttpResponse(f"""
        <h1>Mes groupes preferes sont :</h1>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li
                        </ul>
""")

def view(request):
    return HttpResponse('<h1>A propos</h1> Nous adorons Merch')

def about(request):
    return HttpResponse('A propos')

def listings(request):
    announces=Announce.objects.all()
    return HttpResponse(f"""
            <h1>liste des articles</h1>
            <ul>
                <li>{announces[0].title}</li>
                <li>{announces[1].title}</li>
                <li>{announces[2].title}</li></ul>
""")


def contacts(request):
    return HttpResponse('<h1>Nous contacter!</h1> ')