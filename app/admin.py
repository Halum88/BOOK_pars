
from django.contrib import admin
from .models import Book, Category, Feedback, Author
from .parser import parse_books_from_json

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors_list', 'category_list', 'status']
    actions = ['start_parsing']

    def authors_list(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    def category_list(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    def start_parsing(self, request, queryset):
        parse_books_from_json()
        self.message_user(request, "Парсинг книг успешно завершен.")
    start_parsing.short_description = "Запустить парсинг"

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Author)



