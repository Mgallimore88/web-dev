from django import forms
from app_2.models import User


class NewUserForm(forms.ModelForm):
    # custom validation here
    class Meta: 
        model = User
        fields = '__all__'
