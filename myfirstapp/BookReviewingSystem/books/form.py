from django.forms import ModelForm
from .models import Book
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publish_date', 'author', 'price', 'page_number', 'category']
