from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book,Category,Comments
from .form import CommentForm

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books' : books})

def book_detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request, 'book_detail.html', {'book' : book})

@login_required
def post_comments_controller(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if  form.is_valid():
            comment = form.save(commit=False)
            comment

            return redirect('book_title', pk=pk)
    else:
        comment = CommentForm()
    return render(request, 'comment.html', {'book':book,'form':CommentForm})



