from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import messages
from slugify import slugify

from django.core.paginator import Paginator

from .forms import RegisterForm,ArticleForm


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

def vendre(request):
    form = ArticleForm(request.POST or None, request.FILES)
    if request.method == "POST" and form.is_valid():
        obj=form.save(commit=False)            
        new_slug = form.cleaned_data['article_name']
        obj.slug = slugify(new_slug)
        #obj.seller = {{user.get_username}}
        obj.save()
        return redirect("/eduardo")
    else:
        form = ArticleForm()
    return render(request, "eduardoApp/vendre.html", {
        "form":form
    })


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

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = Article.objects.all()
    categories = Category.objects.all()
    category = request.GET.get('category')
    priceMin = request.GET.get('priceMin')
    priceMax = request.GET.get('priceMax')
    title_contains_query = request.GET.get('title_contains')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(article_name__icontains=title_contains_query)

    if is_valid_queryparam(category) and category!= 'Tous':
        qs = qs.filter(category__name=category)

    if is_valid_queryparam(priceMin):
        qs = qs.filter(price__gte=priceMin)

    if is_valid_queryparam(priceMax):
        qs = qs.filter(price__lt=priceMax)
    return qs


def search(request):
    qs =filter(request)
    paginator = Paginator(qs, 6)

    page = request.GET.get('page')

    qs = paginator.get_page(page)

    title = request.GET.get('title_contains')
    category = request.GET.get('category')
    priceMin = request.GET.get('priceMin')
    priceMax = request.GET.get('priceMax')

   
    context= {
        'categories': Category.objects.all(),
        'queryset':qs,
        'title':title,
        'category': category,
        'priceMin': priceMin,
        'priceMax': priceMax,
        
        }

    return render(request, "eduardoApp/search.html",context)
