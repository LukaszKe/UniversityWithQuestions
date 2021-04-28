from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

    username = None
    email = models.EmailField('email address', unique=True)

    name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)