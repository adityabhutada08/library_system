from django.contrib import admin
from django.urls import path
from library.views import (
    home,
    AuthorListView,
    AuthorCreateView,
    BookListView,
    BookCreateView,
    BorrowRecordListView,
    BorrowRecordCreateView,
    export_to_excel,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # Author-related URLs
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/add/', AuthorCreateView.as_view(), name='add_author'),

    # Book-related URLs
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),

    # Borrow Record-related URLs
    path('borrow-records/', BorrowRecordListView.as_view(), name='borrow_record_list'),
    path('borrow-records/add/', BorrowRecordCreateView.as_view(), name='add_borrow_record'),
    

    # Excel Export
    path('export/', export_to_excel, name='export_excel'),
]
