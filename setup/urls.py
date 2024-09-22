<<<<<<< HEAD
import core
=======

from distutils import core
>>>>>>> 094a617d82c9131fa2dbec39e508b46cb2394086
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
