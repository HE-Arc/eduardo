from django.db import models

# Create your models here.

# --------------- User -----------------
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    user_password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

# ---------------- Articles ---------------
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
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_name

