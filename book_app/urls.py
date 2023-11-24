from rest_framework import routers
from .api import CategoryViewSet, BookViewSet
from django.urls import path
from . import views

'''router_category = routers.DefaultRouter()
router_category.register(r'categories', CategoryViewSet, 'categories')
#urlpatterns = router_category.urls

router_books = routers.DefaultRouter()
router_books.register(r'books', BookViewSet, 'books')
#urlpatterns = router_books.urls

urlpatterns = [
    # Rutas para Categorias
    path('api/', include(router_category.urls)),
    #Rutas para libros
    path('api/', include(router_books.urls)),
]'''

urlpatterns = [
    path('', views.VistaApi, name='home'),
    #RUTAS PARA FUNCION ADD PARA CATEGORY Y LIBROS
    path('categories/create/', views.Add_Categories, name='Add_Categories'),
    path('books/create/', views.Add_Books, name='Add_Books'),
    
    #RUTAS PARA FUNCION SHOW PARA CATEGORY Y LIBROS
    path('categories/', views.show_items, name='show_items'),
    path('books/', views.show_Books, name='show_Books'),

    #RUTAS PARA FUNCION UPDATE PARA CATEGORY Y LIBROS
    path('categories/update/<int:pk>/', views.actualizar_categorias, name='actualizar_categorias'),
    path('books/update/<int:pk>/', views.actualizar_libros, name='actualizar_categorias'),

    #RUTAS PARA FUNCION ELIMINAR PARA CATEGORY Y LIBROS
    path('categories/<int:pk>/delete/', views.eliminar_categorias, name='eliminar_categorias'),    
    path('books/<int:pk>/delete/', views.eliminar_libros, name='eliminar_libros'),
]

