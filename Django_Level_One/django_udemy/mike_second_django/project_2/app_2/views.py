from django.shortcuts import render
from django.http import HttpResponse
from app_2.models import User

# Create your views here.
def index(request):
    return render(request, 'app_2/index.html')

def help(request):
    helpdict = {"help_page": "Help Page!"}
    return render(request, 'app_2/help.html', context=helpdict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'app_2/users.html', context=user_dict)
