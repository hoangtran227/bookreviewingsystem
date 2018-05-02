from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    page_number = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

