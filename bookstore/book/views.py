from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book, Isbn


@login_required
def index(request):
    return render(request, 'book/index.html', {
        "books": Book.objects.all()
    })


@login_required
@permission_required(["book.add_book"], raise_exception=True)
def create(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        book = form.save()
        # ISBN = Isbn.objects.create()
        # book.isbn = ISBN
        book.save()

        return redirect('index')
    return render(request, "book/create.html", {
        "form": form,
    })


@permission_required(["book.edit_book"], raise_exception=True)
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


@permission_required(["book.delete_book"], raise_exception=True)
def delete(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)
    book.delete()
    return redirect('index')


@permission_required(["book.view_book"], raise_exception=True)
def show(request, id):
    return render(request, 'book/show.html', {
        "book": Book.objects.get(pk=id)
    })
