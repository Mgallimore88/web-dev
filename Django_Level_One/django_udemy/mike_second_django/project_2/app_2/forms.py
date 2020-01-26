from django import forms
from app_2.models import User

class UserForm(forms.ModelForm):
    #form fields go here
    class Meta: 
        model = User
        fields = "__all__"