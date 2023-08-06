# my_app/models.py

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategories',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    pageCount = models.IntegerField()
    publishedDate = models.DateTimeField()
    thumbnailUrl = models.URLField()
    shortDescription = models.TextField()
    longDescription = models.TextField()
    status = models.CharField(max_length=10, choices=[('PUBLISH', 'Publish'), ('DRAFT', 'Draft')])
    authors = models.ManyToManyField('Author')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


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
