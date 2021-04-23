from django import forms
from django.core.exceptions import ValidationError

from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("isbn",)

    def clean(self):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        if len(title) < 4 or len(title) > 50:
            raise ValidationError("title must be between 10 to 50 characters!")
        if len(content) < 2:
            raise ValidationError("content must be at least 2 chars!!")
        return self.cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        category = self.cleaned_data.get("name")
        if len(category) < 2:
            raise ValidationError("category must be at least 2 chars!!")
        return category

