from django.db import models
from django.shortcuts import reverse
from django.conf import settings 
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# -------------- Articles ---------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("eduardoApp:category", kwargs={
            'slug':self.slug
        })

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_name = models.CharField(unique=True, max_length=30)
    price = models.FloatField(validators=[MinValueValidator(0)])
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    detail_text = models.TextField(max_length=600, null=True)
    article_image = models.ImageField(upload_to="images/",null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=False, blank=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.article_name

    def get_absolute_url(self):
        return reverse("eduardoApp:detail", kwargs={
            'slug':self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("eduardoApp:add-to-cart", kwargs={
            'slug':self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("eduardoApp:remove-from-cart", kwargs={
            'slug':self.slug
        })


class OrderArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.article_name

    def get_article_total_price(self):
        return self.article.price 

    def get_total_price(self):
        return self.get_article_total_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ManyToManyField(OrderArticle)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for article in self.articles.all():
            total += article.get_total_price()
        return total