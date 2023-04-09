from django.db import models

class Employee (models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=300)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)
