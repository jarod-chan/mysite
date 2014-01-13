from django.shortcuts import render_to_response
from books.models import Book

def booklist(request):
    list = Book.objects.all()
    return render_to_response('booklist.html',{'books':list})
