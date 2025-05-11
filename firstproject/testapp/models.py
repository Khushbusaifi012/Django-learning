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