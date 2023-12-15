from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Causes(models.TextChoices):
    PROPERTY = '1'
    HERITAGE = '2'
    JEALOUSY = '3'
    NOT_UNDERSTANDING = '4'
    OTHER = '5'

class Types(models.TextChoices):
    BROTHERS = '1'
    COUPLE = '2'
    PARENT_AND_CHILD = '3'

class Result(models.TextChoices):
    POSITIVE = '1'
    NEGATIVE = '2'
    ABSTRACT = '3'


class FamilyConflict(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='family_conflicts_imam') 
    comment = models.TextField(blank=True)
    causes = models.CharField(max_length=20, choices=Causes.choices, blank=False)
    types = models.CharField(max_length=20, choices=Types.choices, blank=False)
    results = models.CharField(max_length=20, choices=Result.choices, blank=False)
    date = models.DateField()
    
    class Meta:
        verbose_name = 'Oilaviy muammo '
        verbose_name_plural = 'Oilaviy muammolar '

    def __str__(self):
        return self.imam.username