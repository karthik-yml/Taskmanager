from django.db import models
from tasklist.models import TaskList
# Create your models here.

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
