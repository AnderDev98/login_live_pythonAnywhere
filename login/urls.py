from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_microsoft'),
    path('contact/', views.contact, name='contact'),
]