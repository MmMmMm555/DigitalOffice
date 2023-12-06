from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.employee.models import Employee

# Create your models here.


class Role(models.TextChoices):
    SUPER_ADMIN = 'SUPER_ADMIN'
    REGION_ADMIN = 'REGION_ADMIN'
    DISTRICT_ADMIN = 'DISTRICT_ADMIN'
    IMAM = 'IMAM'
    DEPUTY = 'SUB_IMAM'

class User(AbstractUser):
    first_name = None
    last_name = None
    profil = models.OneToOneField(Employee, unique=True, verbose_name=_("Profil"), on_delete=models.CASCADE, related_name='profil', blank=True, null=True)
    role = models.CharField(max_length=18, choices=Role.choices, default=Role.IMAM, blank=True, null=True)