from django.db import models

# Create your models here.

class Courses(models.Model):
    courseID = models.IntegerField()
    courseNumber = models.IntegerField()
    courseLetters = models.CharField(max_length=3)
    professor = models.CharField(max_length=45)
    homeworkDiff = models.IntegerField()
    lectureDiff = models.IntegerField()
    workLoad = models.IntegerField()
    examDiff = models.IntegerField()

class user(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=75)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=45)
    userName = models.CharField(max_length=75)

class courseTaking(models.Model):
    courseID = models.IntegerField()
    userName = models.CharField(max_length=75)