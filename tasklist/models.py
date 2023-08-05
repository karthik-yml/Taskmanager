from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
