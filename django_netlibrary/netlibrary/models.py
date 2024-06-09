from django.db import models
from django.contrib.postgres.fields.array import ArrayField
from django.contrib.auth.models import User


def default_authors():
    return ['Авторы не указаны']


class Rating(models.Model):
    positive_rating = models.BigIntegerField(verbose_name='Положительный рейтинг', default=0)
    negative_rating = models.BigIntegerField(verbose_name='Отрицательный рейтинг', default=0)
    final_raiting = models.BigIntegerField(verbose_name='Итоговый рейтинг', default=0)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = 'netlibrary_rating'
        managed = True
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Genre(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название жанра')

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'netlibrary_genre'
        managed = True
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги')
    cover = models.ImageField(verbose_name='Обложка', upload_to='covers/')
    book = models.FileField(verbose_name='Книга', upload_to='books/')
    authors = ArrayField(base_field=models.CharField(verbose_name='Автора', max_length=255),
                         blank=True, default=default_authors, verbose_name='Авторы')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    rating = models.OneToOneField('Rating', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'netlibrary_book'
        managed = True
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
