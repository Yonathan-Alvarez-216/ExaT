from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('tablas', tablas, name='tablas'),
    path('updateEmpleado/int:<nombre>', updateEmpleado, name='updareEmpleado'),
]