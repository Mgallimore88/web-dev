from django.shortcuts import render
from app_2.forms import NewUserForm
# from django.http import HttpResponse
# from app_2.models import User

# Create your views here.
def index(request):
    return render(request, 'app_2/index.html')

def help(request):
    helpdict = {"help_page": "Help Page!"}
    return render(request, 'app_2/help.html', context=helpdict)

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        print("Error in form")

    return render(request, 'app_2/users.html', {'form': form})