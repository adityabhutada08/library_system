from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse
import openpyxl

from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm

# Home View
def home(request):
    return render(request, 'library/home.html')

from django.http import HttpResponse
from openpyxl import Workbook
from io import BytesIO
from .models import Book  # or whatever model you're exporting

def export_to_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Books"

    # Header row
    ws.append(["Title", "Author", "Genre", "Published Date"])

    # Data rows
    for book in Book.objects.all():
        ws.append([book.title, book.author.name, book.genre, book.published_date])

    # Save to BytesIO
    virtual_workbook = BytesIO()
    wb.save(virtual_workbook)
    virtual_workbook.seek(0)

    # Create response
    response = HttpResponse(
        virtual_workbook.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=books.xlsx'
    return response


# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10  # Pagination, 10 authors per page
    queryset = Author.objects.all().order_by("name")  # Order authors by name

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('author_list')  # Redirect after form submission


# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 5  # Pagination, 5 books per page

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect after form submission


# Borrow Record Views
class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'library/borrow_record_list.html'
    context_object_name = 'borrow_records'
    paginate_by = 5  # Pagination, 5 records per page

class BorrowRecordCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library/borrow_record_form.html'
    success_url = reverse_lazy('borrow_record_list')  # Redirect after form submission
