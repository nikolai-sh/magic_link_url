from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """
    Class for creating a user registration form based on
    custom user model
    """

    class Meta:
        model = User
        fields = ['email']

class EmailForm(forms.Form):
    """
    Class for creating email form to send magic link. 
    """
    email = forms.EmailField(required=True)