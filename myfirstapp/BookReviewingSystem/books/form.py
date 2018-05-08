from django.forms import ModelForm
from .models import Comments,Book
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publish_date', 'author', 'price', 'page_number', 'category']
