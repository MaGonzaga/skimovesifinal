
from django.contrib import admin
from django.urls import path, include
from .views import hello
from django.conf import settings
from django.conf.urls.static import static
from home import urls as home_urls
from clientes import urls as clients_urls

from corretores import urls as corretores_urls
from itens import urls as itens_urls


from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth.decorators import login_required






urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('clientes/', include(clients_urls)),
    path('corretores/', include(corretores_urls)),
    path('imoveis/', include(itens_urls)),
    path('home', include(home_urls)),
    path('', auth_views.LoginView.as_view(), name='login'),
    
    
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


