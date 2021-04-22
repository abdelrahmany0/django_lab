from django.contrib import admin
from .models import Book
from .models import Category
from .models import Isbn
from .forms import BookForm
from .forms import CategoryForm


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("id", "title", "author")
    list_filter = ("categories",)
    search_fields = ("title",)
    readonly_fields = ("isbn",)


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Isbn)
