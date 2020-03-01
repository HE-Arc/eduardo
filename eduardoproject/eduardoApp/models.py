from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    user_password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Article(models.Model):
    article_name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    state = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_name

