from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from .form import BookForm, CommentForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q

# Create your views here.


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('includes/partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):

    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'includes/partial_book_create.html')


def search(request):
    if request.method == 'GET':
        book_name = request.GET.get('search')
        try:
            status = Book.objects.filter(Q(title__icontains=book_name) | Q(category__name__icontains=book_name))
        except Book.DoesNotExist:
            status = None
        return render(request, "book_list.html", {"books": status})
    else:
        return render(request, "book_list.html", {})


def add_comment_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_book.html', {'form': form})


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('book_detail', pk=comment.book.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('book_detail', pk=comment.book.pk)
