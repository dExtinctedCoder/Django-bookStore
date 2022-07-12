from django import forms
from .models import BookStoreApp

class BookStoreAppForm(forms):
  class Meta:
    model = BookStoreApp
    fields = [
      'tittle',
      'author_name',
      'description',
      'category',
      'book_content'
    ]