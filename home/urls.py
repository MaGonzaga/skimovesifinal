

from django.urls import path
from .views import home, my_logout, home2



urlpatterns = [
    
    path('', home, name="home"),
    path('home2', home2, name="home2"),
    path('logout/', my_logout, name="logout"),

]