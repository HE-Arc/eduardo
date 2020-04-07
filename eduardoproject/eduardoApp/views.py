from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm,ArticleForm


from .models import Article,Category


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

def vendre(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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

    if is_valid_queryparam(category) and category!= 'Choose...':
        qs = qs.filter(category__name=category)

    if is_valid_queryparam(priceMin):
        qs = qs.filter(price__gte=priceMin)

    if is_valid_queryparam(priceMax):
        qs = qs.filter(price__lt=priceMax)

    return qs


def search(request):
    qs =filter(request)
    context= {
        'categories': Category.objects.all(),
        'queryset':qs
        }
    return render(request, "eduardoApp/search.html",context)
