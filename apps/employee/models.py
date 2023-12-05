from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    identity_number = models.CharField(max_length=50)
    phone_number = PhoneNumberField(blank=True)