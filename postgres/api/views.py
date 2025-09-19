from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# Create your views here.


class BooksListCreateView(APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializedBooks = BookSerializer(books,many=True)
            return Response(serializedBooks.data)
        except:
            return Response("Something went wrong")
        
    def post(self,request):
        try:
            serializedData = BookSerializer(data = request.data)
            if serializedData.is_valid():
                serializedData.save()
                return Response(serializedData.data)
            
            return Response(serializedData.errors)
        except:
            return Response("Something went wrong")
    


class BookDetailView(APIView):
    def get(self, request,id):
        try:
            book = Book.objects.get(id = id)
            if book:
                serializedBook = BookSerializer(book)
                return Response(serializedBook.data)
            return Response("Book not found")
        except:
            return Response("Something went wrong")
        
    
    def put(self,request,id):
        try:
            book = Book.objects.get(id = id)
            serializedBook = BookSerializer(book,data = request.data)
            if serializedBook.is_valid():
                serializedBook.save()
                return Response(serializedBook.data)
        
            return Response("Something went wrong")
        except:
            return Response("An error occured while updating")
        

    def delete(self, request, id):
        try:
            book = Book.objects.get(id = id)
            if book:
                book.delete()
                return Response("Book deleted")
            return Response("Book not found")
        except:
            return Response("Something went wrong")