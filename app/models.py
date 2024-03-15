from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_email = models.CharField(max_length=100)
    stu_contact = models.IntegerField(null=True)
    DOB = models.DateField(null=True) 

class Teacher(models.Model):
    tch_name=models.CharField(max_length=100)
    tch_email = models.CharField(max_length=100)
    tch_contact = models.IntegerField(null=True)
    DOB = models.DateField(null=True) 