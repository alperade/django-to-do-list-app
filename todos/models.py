from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL
# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
