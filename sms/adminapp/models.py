from django.db import models

# Create your models here.
from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
from django.contrib.auth.models import User
class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    User=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Register_Number



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    experience = models.CharField(max_length=20)
    usability = models.CharField(max_length=20)
    features = models.CharField(max_length=200, blank=True)
    comments = models.TextField(blank=True)
    recommend = models.CharField(max_length=3)  # 'Yes' or 'No'

    def __str__(self):
        return f"Feedback from {self.name}"

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name




