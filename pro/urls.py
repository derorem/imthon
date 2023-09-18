from django.contrib import admin
from django.urls import path
from app.views import toddo,delate,editodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',toddo),
    path('/delate/<int:id>/',delate),
path('edit/<int:a>/',editodo)
]




