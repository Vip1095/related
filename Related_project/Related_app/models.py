from django.db import models

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=120)


class Books(models.Model):
    book_name = models.CharField(max_length=120)
    written_by = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors")
    helped_by = models.ForeignKey(Author,on_delete=models.CASCADE, related_name="helped_author")