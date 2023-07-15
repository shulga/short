from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').select_related('category').select_related('author__country').prefetch_related('tags').all()
    serializer_class = BookSerializer
