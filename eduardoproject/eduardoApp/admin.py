from django.contrib import admin

from .models import Article, Category, OrderArticle, Order, State, Color

# Register your models here.

admin.site.register(Category)
admin.site.register(State)
admin.site.register(Color)
admin.site.register(Article)
admin.site.register(Order)
admin.site.register(OrderArticle)
