from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    fee=models.IntegerField()

