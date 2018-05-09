from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(null=True)
    author = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(default=0)
    page_number = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000, default='This is content of the book')
    ratings = models.ManyToManyField(User, through='BookRating')

    class Meta:
        db_table = 'book'


    def __str__(self):
        return self.title


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    class meta:
        unique_together = ('book','user')
