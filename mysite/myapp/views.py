from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "myapp/index.html")


def brian(request):
    return HttpResponse("Hello, Brian.")


def greed(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
