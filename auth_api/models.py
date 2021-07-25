from django.db import models

class UserData(models.Model):
    username = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email  = models.EmailField()
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=250)


    def __str__(self):
        return str(self.username)
