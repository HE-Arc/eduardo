from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    article_name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    state = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    seller = models.ForeignKey(
        User,
        null = True,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.article_name

