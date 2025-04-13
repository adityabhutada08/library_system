from django.urls import path
from . import views
from .views import (
    home,
    AuthorCreateView, AuthorListView,
    BookCreateView, BookListView,
    BorrowRecordCreateView, BorrowRecordListView,
    export_data,  # <-- ensure this exists in views.py
)

urlpatterns = [
    path('', home, name='home'),

    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/add/', AuthorCreateView.as_view(), name='author-add'),
    path('add/', views.add_author, name='add-author'),

    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),

    path('borrow-records/', BorrowRecordListView.as_view(), name='borrowrecord-list'),
    path('borrow-records/add/', BorrowRecordCreateView.as_view(), name='add_borrow_record'),


    path('export/', export_data, name='export-data'),
]
