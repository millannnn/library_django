from rest_framework import serializers
from .models import Category, Book

'''Estos serializadores permiten que django rest framework
conviertan automaticamente los objetos category o book en un JSON y viceversa
esto facilita el envio y la recepcion de datos a traves de la API'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', )
        read_only_fields = ('created_at', )

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'author', 'Category', 'created_at', )
        read_only_fields = ('created_at', )