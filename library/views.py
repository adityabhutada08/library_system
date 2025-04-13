from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm

class AddAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/add_author.html'
    success_url = reverse_lazy('list-authors')

class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/add_book.html'
    success_url = reverse_lazy('list-books')

class AddBorrowRecordView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library/add_borrow_record.html'
    success_url = reverse_lazy('list-borrow-records')

class AuthorListView(ListView):
    model = Author
    template_name = 'library/list_authors.html'
    context_object_name = 'authors'
    paginate_by = 5

class BookListView(ListView):
    model = Book
    template_name = 'library/list_books.html'
    context_object_name = 'books'
    paginate_by = 5

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'library/list_borrow_records.html'
    context_object_name = 'borrow_records'
    paginate_by = 5
