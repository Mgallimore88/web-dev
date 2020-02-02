from django.shortcuts import render
from app_2.models import User
from app_2.forms import UserForm

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

def adduser(request):
    user_form = UserForm()
    user_form_dict = {'userform': user_form}
    if request.method=='POST':
        print("hi")
        # Create a form instance from POST data
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # Save a new User object from the form's data
            user_form.save(commit=True)
            return users(request)
        else:
            print('error invalid form')




    return render(request, 'app_2/userform.html', context=user_form_dict)
