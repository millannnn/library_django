from .models import * # se importa los modelos de la aplicacion book_app del archivo models.py
from rest_framework import viewsets, permissions # se importa los modulos , view sets, y permissions de django rest framework
from .serializers import * # importa los serializadores que definimos en serializers.py
'''
La clase CategoryViewset hereda de viewsets.modelviewsets,
lo que significa que proporciona operaciones crud completas 
para el modelo Category.
'''
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # se define el conjunto de datos que esta vista manejara
    permission_classes = [permissions.AllowAny] # esto establece las clases de permisos para la vista, en este caso, allowAny significa que cualquier usuario autenticado o no puede acceder a esta vista.
    serializer_class = CategorySerializer # establece la clase de serializador para la vista, el serializador define como se convierten los objetos del modelo category en JSON para ser enviados a traves de la API
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer