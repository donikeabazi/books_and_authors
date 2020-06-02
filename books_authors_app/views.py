from django.shortcuts import render, redirect
from .models import Book
from .models import Author
# Create your views here.
def index(request):
    if request.POST:
        title = request.POST['title']
        desc = request.POST['description']
        Book.objects.create(title=title,desc=desc)
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def authors(request):
    if request.POST:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(first_name=fname,last_name=lname,notes=notes)
    context ={
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def author(request, id):
    curr_author = Author.objects.get(id=id)
    if request.POST:
        book=request.POST['book']
        curr_author.books.add(book)
    context ={
        "author": Author.objects.get(id=id),
        "author_books": Author.objects.get(id=id).books.all(),
        "other_books": Book.objects.exclude(books=curr_author).all()
    }
    return render(request, "author.html", context)

def book(request, id):
    curr_book = Book.objects.get(id=id)
    if request.POST:
        author=request.POST['author']
        curr_book.books.add(author)
    context = {
        "book": Book.objects.get(id=id),
        "book_authors": Book.objects.get(id=id).books.all(),
        "other_authors": Author.objects.exclude(books=curr_book).all()
    }
    return render(request, "book.html", context)