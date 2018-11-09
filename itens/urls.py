

from django.urls import path
from .views import casa_list
from .views import casa_new
from .views import casas_delete
from .views import casas_update



urlpatterns = [
    
    path('list/', casa_list, name="casas_list"),
    path('new/', casa_new, name="casas_new"),
    path('update/<int:id>/', casas_update, name="casas_update"),
    path('delete/<int:id>/', casas_delete, name="casas_delete"),
] 
