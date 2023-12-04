from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseModel

# Create your models here.


class Role(BaseModel):
    title = models.CharField(max_length=255)


class User(AbstractUser):
    first_name = None
    last_name = None
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, blank=True, null=True
    )
