from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),

]
