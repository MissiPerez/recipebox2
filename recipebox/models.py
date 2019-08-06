from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return f"prepared by {self.name}"


class RecipeTitle(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time = models.CharField(max_length=30)
    instructions = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.title} - {self.author}"
