from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .form import BookForm
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




