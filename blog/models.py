from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    date_hired = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = "employee"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"