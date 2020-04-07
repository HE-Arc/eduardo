from django.urls import path, include

from . import views

app_name = 'eduardoApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<slug>/', views.DetailView.as_view(), name='detail'), 
    path("vendre/", views.vendre, name="vendre"),
]
