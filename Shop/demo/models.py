
from django.db import models
from datetime import datetime  
class Person(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(default="")
  phno = models.IntegerField(default=1)
  Date= models.DateField(default=datetime.now())
