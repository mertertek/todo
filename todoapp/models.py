import datetime
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE,)
    todo_name = models.CharField(max_length=100)
    todo_date = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_name
