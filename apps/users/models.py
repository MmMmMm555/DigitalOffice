from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseModel

# Create your models here.


class Role(models.TextChoices):
    SUPER_ADMIN = 'SUPER_ADMIN'
    REGION_ADMIN = 'REGION_ADMIN'
    DISTRICT_ADMIN = 'DISTRICT_ADMIN'
    IMAM = 'IMAM'
    SUB_IMAM = 'SUB_IMAM'



class User(AbstractUser):
    first_name = None
    last_name = None
    role = models.CharField(
        max_length=18, choices=Role.choices, default=Role.IMAM, blank=True, null=True
    )
