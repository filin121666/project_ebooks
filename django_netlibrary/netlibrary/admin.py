from django.contrib import admin

from .models import Rating, Genre, Book

admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Book)