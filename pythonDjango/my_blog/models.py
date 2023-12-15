from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    release_date = models.DateField("Date", default=date.today)
    #num_stars = models.IntegerField(max_length=50)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
