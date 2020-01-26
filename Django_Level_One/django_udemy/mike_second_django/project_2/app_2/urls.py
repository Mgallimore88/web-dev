from django.urls import path
from app_2 import views


urlpatterns = [
    path('help/', views.help, name='help'),
    path('userform/', views.adduser, name='adduser'),
    path('', views.users, name='users')
]
