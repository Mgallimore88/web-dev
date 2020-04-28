from django.urls import path
from . import views

# TEMPLATE URLS - Tell django where the templates live for this app
app_name = 'basic_app'

urlpatterns=[
    path('register/', views.register,name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('special/', views.special, name='special')
]