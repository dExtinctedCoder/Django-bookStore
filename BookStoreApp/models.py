from django.db import models

# Create your models here.


class BookStoreApp(models.Model):
  tittle = models.CharField(max_length=255);
  author_name = models.CharField(max_length=100);
  description = models.BigAutoField(max_length=255);
  category = models.CharField(max_length=100);
  pub_date = models.DateField(auto_now_add=True)
  book_content = models.BigAutoField();

