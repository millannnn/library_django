from rest_framework import routers # importa el modulo routers de django rest framework, queproporciona una forma sencilla de definir rutas url para las vistas.
from .api import * #importamos todas las vistas que definimos en el archivo api.py

router = routers.DefaultRouter() # crea una nueva instancia de defaultrouter, que es una clase de enrutador que automaticamente crea rutas url para las vistas, basandose en los metodos que definen.
router.register('api/categories', CategoryViewSet, 'categories') # registra la vista categoryviewset con el enrutador bajo la ruta URL api/categories.el tercer argumento 'categories' es un nombre opcional que se puede usar para referirse a esta ruta url en otras partes del codigo

router.register('api/books', BookViewSet, 'books')
urlpatterns = router.urls #asigna las rutas URL generadas por el enrutador a urlpatterns, que es la variable que django utiliza para determinar las rutas url de la aplicacion
