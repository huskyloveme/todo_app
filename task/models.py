from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=225)
    deadline = models.DateTimeField(default=datetime.now())
    assigned_to = models.ManyToManyField(User)

    def __str__(self):
        return self.title