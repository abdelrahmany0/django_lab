from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=2048)

    def __str__(self):
        return self.title
