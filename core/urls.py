
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_view, name='base'),
    path('form', views.form_view, name='form'),
]