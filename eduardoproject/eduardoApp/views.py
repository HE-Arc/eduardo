from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

from .models import Article

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'eduardoApp/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('article_name')

class DetailView(generic.DetailView):
    model = Article
    template_name = 'eduardoApp/detail.html'

def vendre(response):
    return render(response, "eduardoApp/vendre.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})

def logout(response):
    auth.logout(respnse)
    messages.info(response, "Logged out successfully!")
    return redirect("/eduardo")

