from django import forms
from django.contrib.auth.forms import UserCreationForm
from my_app.models import MyUser


class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=13, required=True)
    password1 = forms.CharField(max_length=13, required=True)
    password2 = forms.CharField(max_length=13, required=True)

    class Meta:
        model = MyUser
        fields = ('phone', 'email', 'password1', 'first_name', 'last_name')
