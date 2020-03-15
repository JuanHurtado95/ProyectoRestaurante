"""RestauranteChino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionPedidos import views
from gestionPedidos.views import home,loginUser,menu

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #path('', home.as_view(), name='home'),
    path('casa/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('busqueda_ingredientes/', views.busqueda_ingredientes, name='busqueda_ingredientes'),
    path('buscar/', views.buscar, name='buscar'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.loginUser, name='login'),
    path('login/registro/', views.registroUser),
    path('menu/', views.menu, name='menu'),

]
