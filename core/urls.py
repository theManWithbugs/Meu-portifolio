
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('form', views.form_view, name='form'),
    path('meu_perfil/', views.perfil_view, name='perfil'),
]