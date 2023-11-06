
from .models import *
from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="выберите дату рожджения",
    )
    class Meta:
        model = CustomUser
        fields = ['full_name','birth_date', 'username', 'password1', 'password2']
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'article']
