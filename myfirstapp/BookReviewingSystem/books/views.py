from django.shortcuts import render, get_object_or_404
from .models import Book,Category

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books' : books})

def book_detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request, 'book_detail.html', {'book' : book})



