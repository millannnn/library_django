from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer
from django.shortcuts import get_object_or_404
'''
@api_view(['GET','POST'])
def category_view(request):
    
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data)
        
    elif request.method == 'POST':
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer).data
        return Response(category_serializer.errors)
    
@api_view(['GET','POST'])
def book_view(request):
    
    if request.method == 'GET':
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data)
        
    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer).data
        return Response(book_serializer.errors)
'''
#------------------------------------------------------------------------------#
#DOCUMENTACION DJANGO
'''@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)'''


#------------------------------------------------------------------------#
#FUNCION DE TIPO GET PARA MOSTRAR LISTADO DE OPCIONES BRO
@api_view(['GET'])
def VistaApi(request):
    api_urls = {
        'Category': {
            'All Categories': 'categories',
            'Add Category': 'categories/create',
            'Update Categories': 'categories/update/pk',
            'Delete Categories': 'categories/pk/delete'
        },
        'Books': {
            'All Books': 'books',
            'Add Book': 'books/create',
            'Update Book': 'books/update/pk',
            'Delete Book': 'books/pk/delete'
        }
    }

    return Response(api_urls)

#---------------------------------------------------------------------------#
#FUNCION ADD DE TIPO POST PARA AGREGAR CATEGORIAS BRO
@api_view(['POST','GET'])
def Add_Categories(request):
    Categories = CategorySerializer(data=request.data)

    # validating for already existing data
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if Categories.is_valid():
        Categories.save()
        return Response(Categories.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#---------------------------------------------------------------------------------#
#FUNCION ADD DE TIPO POST PARA AGREGAR LIBROS BRO
@api_view(['POST','GET'])
def Add_Books(request):
    Books = BookSerializer(data=request.data)

    # validating for already existing data
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if Books.is_valid():
        Books.save()
        return Response(Books.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------------------------------------------------#
#FUNCION SHOW DE TIPO GET PARA VER TODAS LAS CATEGORIAS BRO
@api_view(['GET'])
def show_items(request):
	
	
	# checking for the parameters from the URL
	if request.query_params:
		show = Category.objects.filter(**request.query_params.dict())
	else:
		show = Category.objects.all()

	# if there is something in items else raise error
	if show:
		serializer = CategorySerializer(show, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------------------------------------------------#
#FUNCION SHOW DE TIPO GET PARA VER TODOS LOS LIBROS BRO
@api_view(['GET'])
def show_Books(request):
	
	
	# checking for the parameters from the URL
	if request.query_params:
		showl = Book.objects.filter(**request.query_params.dict())
	else:
		showl = Book.objects.all()

	# if there is something in items else raise error
	if showl:
		serializer = CategorySerializer(showl, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

#----------------------------------------------------------------------#
#FUNCION PARA ACTUALIZAR CATEGORIAS
@api_view(['GET','POST'])
def actualizar_categorias(request, pk):
    item = Category.objects.get(pk=pk)
    data = CategorySerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#----------------------------------------------------------------------#
#FUNCION PARA ACTUALIZAR LIBROS
@api_view(['GET','POST'])
def actualizar_libros(request, pk):
    item = Book.objects.get(pk=pk)
    data = BookSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#----------------------------------------------------------------------#
#FUNCION PARA ELIMINAR CATEGORIAS

@api_view(['DELETE','GET','POST'])
def eliminar_categorias(request, pk):
    item = get_object_or_404(Category, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#----------------------------------------------------------------------#
#FUNCION PARA ELIMINAR LIBROS

@api_view(['DELETE','GET','POST'])
def eliminar_libros(request, pk):
    item = get_object_or_404(Book, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)