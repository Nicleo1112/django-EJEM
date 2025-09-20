from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='')
    username = forms.CharField(max_length=150, help_text='')
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput,
        help_text=''
    )
    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput,
        strip=False,
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity']