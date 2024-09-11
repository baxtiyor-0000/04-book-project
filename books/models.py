from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    isbn_number = models.CharField(max_length=13)
    pages = models.PositiveIntegerField()
    lang = models.CharField(max_length=30)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
