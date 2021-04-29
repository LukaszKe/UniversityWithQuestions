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
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)

class University(models.Model):

    class UniversityName(models.TextChoices):
        POLITECHNIKA_WROCLAW = 'PWR', 'Politechnika Wrocławska'
        POLITECHNIKA_WARSZAWA = 'PW', 'Politechnika Warszawska'
        POLITECHNIKA_SZCZECIN = 'ZUT', 'Zachodniopomorski Uniwersytet Technologiczny'

    class City(models.TextChoices):
        WARSZAWA = 'WAW', 'Warszawa'
        SZCZECIN = 'SZN', 'Szczecin'
        WROCLAW = 'WRO', 'Wrocław'

    name = models.CharField(max_length = 50)

    city = models.CharField(max_length = 20)

    description = models.TextField()

    def __str__(self):
        return self.name