from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

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
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    email      = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug  = models.SlugField(max_length=250)
    body  = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status =models.CharField(max_length = 2, choices = Status, default = Status.DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_nametim='blog_posts')
    class Meta:
        ordering = ('-publish',)
        db_table = 'title'
    indxs = [
        models.Index(fields=['-publish'])
    ]

    def __str__(self):
        return self.title
    



class FavouritePost(models.Model):
    pk = models.CompositePrimaryKey(
        'user', 'post'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    
    post = models.ForeignKey(
        'blog.Post',
        on_delete= models.CASCADE
    )
    created = models.DateTimeField(auto_now_add = True)
    





