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
  success_url = 'list_books.html';

  def __str__(self):
    return self.tittle;

