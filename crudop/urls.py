from django.urls import path
from .views import CreateTask, DeleteTask, ViewAllTask, ViewTask, UpdateTask

urlpatterns = [
    path("crud/create", CreateTask.as_view(), name="CreateTask"),
    path("crud/update/<int:id>", UpdateTask.as_view(), name="UpdateTask"),
    path("crud/delete/<int:id>", DeleteTask.as_view(), name="DeleteTask"),
    path("crud/view/<int:id>", ViewTask.as_view(), name="ViewTask"),
    path("crud/ViewAll", ViewAllTask.as_view(), name="ViewAllTask"),
]
