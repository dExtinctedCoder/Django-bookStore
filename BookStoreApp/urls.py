from django import views
from django.urls import path
from .views import CreateBook, DeleteBook, DetailBooks, EditBook, HomePage, ListBooks


urlpatterns = [
    path('', HomePage.as_view()),
    path('create/', CreateBook.as_view()),
    path('list/', ListBooks.as_view()),
    path('detail/'+ '<pk>', DetailBooks.as_view()),
    path('edit/'+ '<pk>', EditBook.as_view()),
    path('delete/'+'<pk>', DeleteBook.as_view())
]