from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user

class Tasklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.user}'


    def save(self, *args, **kwa):
        user = get_current_user()
        if user and not user.pk: # checking for  also deleted user if he is able to acces the api because of session
            user = None
        if not self.pk:
            self.user = user
        return super(Tasklist, self).save(*args, **kwa)