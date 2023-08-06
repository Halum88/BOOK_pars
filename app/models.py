# my_app/models.py

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"From: {self.name}, Email: {self.email}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    pageCount = models.IntegerField(blank=True, null=True)
    publishedDate = models.DateTimeField(default=timezone.now, blank=True, null=True)
    thumbnailUrl = models.URLField(blank=True, null=True)
    shortDescription = models.TextField(blank=True, null=True)
    longDescription = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('PUBLISH', 'Publish'), ('DRAFT', 'Draft')])
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title