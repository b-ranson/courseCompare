from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission

from .decorators import *

# Create your models here.

class Courses(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseNumber = models.IntegerField()
    courseName = models.CharField(max_length=75)
    courseLetters = models.CharField(max_length=3)
    professor = models.CharField(max_length=45)
    homeworkDiff = models.IntegerField()
    lectureDiff = models.IntegerField()
    workLoad = models.IntegerField()
    examDiff = models.IntegerField()
    numOfRatings = models.IntegerField(default = 0)

class CourseTaking(models.Model):
    courseID = models.IntegerField()
    username = models.CharField(max_length=75)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        group = Group.objects.get(name="BASEUSER")
        user.groups.add(group)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have staff true")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have superuser true")

        return self.create_user(email=email, password=password, **extra_fields)       

class MyCustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=75, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)


    objects = CustomUserManager()
    USERNAME_FIELD = "username"
 
    def __str__(self):
        return self.username
    
class CustomGroup(Group):
    description = models.TextField(blank=True)