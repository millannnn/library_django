from .models import Category
from .models import Book
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer
from .serializers import BookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer