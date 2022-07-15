from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BookStoreApp


class HomePage(CreateView):
  model = BookStoreApp
  template_name = 'home.html'
  fields = []


class CreateBook(CreateView):
  model = BookStoreApp
  fields = [
    'tittle',
    'author_name',
    'description',
    'category',
    'book_content'
  ]

  template_name = 'create_books.html';
  success_url = '/list';

  def __str__(self):
    return self.tittle;


class ListBooks(ListView):
  model = BookStoreApp
  fields = [
    'tittle',
    'author_name',
    'category',
  ]
  template_name = 'list_books.html'


class DetailBooks(DeleteView):
  model = BookStoreApp
  template_name = 'detail_books.html'


class EditBook(UpdateView):
  model = BookStoreApp;
  fields = [
    'tittle',
    'description',
    'category',
    'book_content'
  ]
  template_name = 'edit_books.html';
  success_url = '/list';


class DeleteBook(DeleteView):
  model = BookStoreApp;
  template_name = 'delete_books.html';
  success_url = '/list'