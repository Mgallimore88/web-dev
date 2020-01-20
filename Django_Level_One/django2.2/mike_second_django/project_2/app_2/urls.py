from django.urls import path
from app_2 import views
urlpatterns = [
    path('', views.help, name='help')
]