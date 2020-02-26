from django.shortcuts import render

# views.py file
from django.http import HttpResponse
from . import urls


def index(response):
    return render(response,"main/base.html",{})

def home(response):
    return render(response,"main/home.html",{})
