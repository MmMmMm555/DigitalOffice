from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.employee.models import Employee
from apps.common.regions import Regions, Districts
from django.contrib.auth.hashers import make_password

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
    region = models.ForeignKey(
        Regions, on_delete=models.SET_NULL, blank=True, null=True, related_name='region')
    district = models.ForeignKey(
        Districts, on_delete=models.SET_NULL, blank=True, null=True, related_name='district')
    profil = models.OneToOneField(Employee, unique=True, verbose_name=_(
        "Profile"), on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    role = models.CharField(
        max_length=18, choices=Role.choices, default=Role.IMAM, blank=True, null=True)

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        user = User.objects.create(
            email=email,
            username=username,
            password=make_password(password))
        return user

    def __str__(self) -> str:
        return self.username
