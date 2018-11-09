

from django.urls import path
from .views import corre_list
from .views import corre_new
from .views import corre_update
from .views import corre_delete



urlpatterns = [
    
    path('list/', corre_list, name="corre_list"),
    path('new/', corre_new, name="corre_new"),
    path('update/<int:id>/', corre_update, name="corre_update"),
    path('delete/<int:id>/', corre_delete, name="corre_delete"),
] 
