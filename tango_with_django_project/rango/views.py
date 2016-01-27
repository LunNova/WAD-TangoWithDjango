from django.http import HttpResponse
from django.shortcuts import render

def renderTemplate(request, template, context = None):
    return render(request, 'rango/' + template, context)

def index(request):
    return renderTemplate(request, "index.html", {'boldmessage': "I am bold font from the context"})

def about(request):
    return renderTemplate(request, "about.html")
