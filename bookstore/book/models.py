import uuid

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Isbn(models.Model):
    Isbn = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, blank=True)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
