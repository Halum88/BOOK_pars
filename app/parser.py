import json
from .models import Book, Category, Author
from django.conf import settings
import os


def parse_books_from_json():
    json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/app/books.json')  
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            title = item.get('title', '')
            isbn = item.get('isbn', '')
            pageCount = item.get('pageCount', '')
            publishedDate = item.get('publishedDate', {}).get('$date', None)
            thumbnailUrl = item.get('thumbnailUrl', '')
            shortDescription = item.get('shortDescription', '')
            longDescription = item.get('longDescription', '')
            status = item.get('status')

            # Создаем или получаем объект категории
            categories = item.get('categories', [])
            book_categories = []
            for category in categories:
                category_obj, _ = Category.objects.get_or_create(name=category)
                book_categories.append(category_obj)

            # Создаем или получаем объект автора
            authors = item.get('authors', [])
            book_authors = []
            for author in authors:
                author_obj, _ = Author.objects.get_or_create(name=author)
                book_authors.append(author_obj)

            # Добавляем книгу в базу данных
            book = Book.objects.create(
                title=title,
                isbn=isbn,
                pageCount=pageCount,
                publishedDate=publishedDate,
                thumbnailUrl=thumbnailUrl,
                shortDescription=shortDescription,
                longDescription=longDescription,
                status=status,
            )

            # Добавляем связи с категориями и авторами
            book.categories.add(*book_categories)
            book.authors.add(*book_authors)
            book.save()
