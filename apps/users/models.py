from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.employee.models import Employee
from apps.common.regions import Regions, Districts

# Create your models here.


class Role(models.TextChoices):
    SUPER_ADMIN = '1'
    REGION_ADMIN = '2'
    DISTRICT_ADMIN = '3'
    IMAM = '4'
    SUB_IMAM = '5'


class User(AbstractUser):
    first_name = None
    last_name = None
    region = models.ForeignKey(Regions, on_delete=models.SET_NULL, blank=True, null=True, related_name='region')
    district = models.ForeignKey(Districts, on_delete=models.SET_NULL, blank=True, null=True, related_name='district')
    profil = models.OneToOneField(Employee, unique=True, verbose_name=_("Profil"), on_delete=models.CASCADE, related_name='profil', blank=True, null=True)
    role = models.CharField(max_length=18, choices=Role.choices, default=Role.IMAM, blank=True, null=True)