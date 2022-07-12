from django import views
from django.urls import path
from .views import CreateBook, HomePage


urlpatterns = [
    path('', HomePage.as_view()),
    path('create/', CreateBook.as_view())
]