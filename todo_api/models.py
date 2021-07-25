from django.db import models
from auth_api.models import UserData

class Todo(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    writer = models.ForeignKey(UserData, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.title)