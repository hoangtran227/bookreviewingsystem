from .models import Book, Comment
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publish_date', 'author', 'price', 'page_number', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content']
