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

    def __str__(self):
        return self.title


class Comments(models.Model):
    comments = models.TextField()
    created_by = models.ForeignKey(User, related_name='Comments', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
