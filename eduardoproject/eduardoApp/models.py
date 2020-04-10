from django.db import models
from django.shortcuts import reverse
from django.conf import settings 

# Create your models here.

# -------------- Articles ---------------
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    state = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    detail_text = models.TextField(max_length=600, null=True)
    article_image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField()

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
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.article.article_name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ManyToManyField(OrderArticle)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username
