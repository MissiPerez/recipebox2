from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecipeTitle(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time = models.CharField(max_length=30)
    instructions = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.title} - {self.author}"
