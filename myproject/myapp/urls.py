# myapp/urls.py
from django.urls import path
from .views import index, create, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
]
