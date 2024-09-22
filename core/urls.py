
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_view, name='base'),
    path('form', views.form_view, name='form'),
<<<<<<< HEAD
    path('meu_perfil/', views.perfil_view, name='perfil'),
=======
>>>>>>> 094a617d82c9131fa2dbec39e508b46cb2394086
]