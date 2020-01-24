from django import forms

class UserData(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=256)
    text = forms.CharField(widget=forms.Textarea)

    