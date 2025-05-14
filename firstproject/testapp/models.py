from django.db import models

# Create your models here.
class Employee(models.Model):   #employee model
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)

class Student(models.Model):    #student model
    sno=models.IntegerField()
    sname=models.CharField(max_length=20)
    subjects=models.CharField(max_length=20)
    percentage=models.FloatField()

class College(models.Model):    #college model
    name=models.CharField(max_length=20)
    college_name=models.CharField(max_length=20)
    subjects=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    mobilenumber=models.IntegerField()

class Address(models.Model):   #Address model
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
