from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book


def index(request):
    return render(request, 'book/index.html', {
        "books": Book.objects.all()
    })


def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, "book/create.html", {
        "form": form
    })


def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'book/edit.html', {
        "form": form,
        "book": book
    })


def delete(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    book.delete()
    return redirect('index')


def show(request, id):
    return render(request, 'book/show.html', {
        "book": Book.objects.get(pk=id)
    })
