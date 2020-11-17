from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Roles(models.Model):
    title = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.title

class Employee(models.Model):
    full_name = models.CharField(max_length=100,null=False,blank=False)
    emp_code = models.CharField(max_length=3,null=False,blank=False)
    mobile = models.CharField(max_length=15,null=False,blank=False)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
