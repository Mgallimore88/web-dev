from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("My Second App... <em>update in real time!</em>")

def help(request):
    helpdict = {"help_page": "Help Page!"}
    return render(request, 'app_2/help.html', context=helpdict)
