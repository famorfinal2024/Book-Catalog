from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def list(self, request, *args, **kwargs):
   response = super().list(request, *args, **kwargs)
   return Response({
       "message": "List of books retrieved successfully",
       "data": response.data
    }
    
    )