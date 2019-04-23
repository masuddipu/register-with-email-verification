from django import forms
from .models import  UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        exclude = ('user',)
