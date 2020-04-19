from django.urls import path, include

from . import views

app_name = 'eduardoApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<slug>/', views.DetailView.as_view(), name='detail'), 
    path("vendre/", views.VendreView.as_view(), name="vendre"),
    path('profile',views.ProfileView.as_view(),name='profile'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path("search/", views.search, name="search"),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('validate-order/', views.validate_order, name="validate-order"),
]
