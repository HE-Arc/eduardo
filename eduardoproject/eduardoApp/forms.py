from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields=["username","email","password1","password2"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["article_name", "category", "price", "quantity", "state", "color", "detail_text", "article_image"]