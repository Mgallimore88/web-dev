from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'basicform/welcome.html')

def user_data_form_view(request):
    form = forms.UserData()
    if request.method == 'POST':
        form = forms.UserData(request.POST)

        #check to see if the form is valid
        if form.is_valid():
            print('Form Validation Success')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'basicform/userdata.html', {'form': form})
