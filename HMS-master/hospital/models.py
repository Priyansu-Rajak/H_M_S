from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    email = models.CharField(max_length=100,default=True)
    age = models.IntegerField(null=True)
    fees = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    treatment = models.CharField(max_length=100,default=True)
    gender = models.CharField(max_length=100)

    class Meta:
        db_table = 'patient'

class Login(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'login'
