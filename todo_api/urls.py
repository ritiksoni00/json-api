from django.urls import path, include
from .views import GetAllTodo, CreatTodo,DeleteTodo, UpdateTodo, GetTodo
urlpatterns = [
    path('alltodos/', GetAllTodo.as_view(), name='GetAllTodo'),
    path('create/', CreatTodo.as_view(), name='createtodo'),
    path('get/<int:id>', GetTodo.as_view(), name='GetTodo' ),
    path('update/<int:id>', UpdateTodo.as_view(), name='UpdateTodo'),
    path('delete/<int:id>', DeleteTodo.as_view(), name='DeleteTodo'),
]