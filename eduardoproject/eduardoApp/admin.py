from django.contrib import admin

from .models import Article, Category, OrderArticle, Order


# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Order)
admin.site.register(OrderArticle)
