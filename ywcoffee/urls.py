from django.urls import path  
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('home/', views.site_view, name='home'),
    path('coffee/', views.coffee_view, name='coffee'),
]

