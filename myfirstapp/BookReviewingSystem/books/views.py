from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.models import User
from .models import Book, Category, Comments
from .form import CommentForm,BookForm
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.


def book_list(request) :
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books' : books })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book' : book })

@login_required
def post_comments_controller(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if  form.is_valid():
            comment = form.save(commit=False)
            return redirect('book_title', pk=pk)
    else:
        comment = CommentForm()
    return render(request, 'comment.html', {'book':book,'form':CommentForm})


def search(request) :
    books = Book.objects.filter(title__contains=request)
    search = request.GET.get('q')
    return render(request, 'book_list.html', {'book' : books})

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
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'includes/partial_book_create.html')

