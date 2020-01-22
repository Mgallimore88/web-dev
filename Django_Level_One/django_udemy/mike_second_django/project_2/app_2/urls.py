from django.urls import path
from app_2 import views


urlpatterns = [
    path('help/', views.help, name='help'),
    path('', views.users, name='users')
]
