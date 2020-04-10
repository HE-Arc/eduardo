from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import messages

from .forms import RegisterForm

from .models import Article, Category, Order, OrderArticle

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'eduardoApp/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('article_name')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] =Category.objects.all()
        return context

class DetailView(generic.DetailView):
    model = Article
    template_name = 'eduardoApp/detail.html'


class CartListView(generic.ListView):
    template_name = 'eduardoApp/cart.html'
    context_object_name = 'ordered_articles_list'



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

def logout_view(response):
    logout(response)
    return redirect("/eduardo")

def get_categories(request):
    category_list=Category.objects.all()
    context = {'category_list':category_list}
    return render(request,'eduardoApp/index.html',context)

def add_to_cart(request, slug):
    article = get_object_or_404(Article, slug=slug)
    order_article, created = OrderArticle.objects.get_or_create(
        article=article,
        user=request.user,
        ordered=False
        )
    order_set = Order.objects.filter(user=request.user, ordered=False)
    if order_set.exists():
        order=order_set[0]
        if order.articles.filter(article__slug=article.slug).exists():
            order_article.quantity += 1
            order_article.save()
            messages.info(request, "Quantité mise à jour")

        else:
            messages.info(request, "Article ajouté au panier")
            order.articles.add(order_article)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date = ordered_date)
        order.articles.add(order_article)
        messages.info(request, "Article ajouté au panier")    
    return redirect('eduardoApp:detail', slug=slug)

def remove_from_cart(request, slug):
    article = get_object_or_404(Article, slug=slug)
    order_set = Order.objects.filter(user=request.user, ordered=False)
    if order_set.exists():
        order=order_set[0]
        if order.articles.filter(article__slug=article.slug).exists():
            order_article = OrderArticle.objects.filter(
                article=article,
                user=request.user,
                ordered=False
            )[0]
            order_article.quantity -=1
            order.articles.remove(order_article)   
            messages.info(request, "Article supprimé du panier")  
            return redirect("eduardoApp:detail", slug=slug)   
        else:
            messages.info(request, "Article non présent dans le panier")
            return redirect("eduardoApp:detail", slug=slug)

    else:
        messages.info(request, "Panier vide")
        return redirect("eduardoApp:detail", slug=slug)
