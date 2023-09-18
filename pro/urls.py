from django.contrib import admin
from django.urls import path
from app.views import todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo)
]
