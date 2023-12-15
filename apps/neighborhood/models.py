from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Participants(models.TextChoices):
    TEENS = '1'
    WOMANS = '2'
    MANS = '3'
    OLDER_MAN = '4'
    MIX = '5'

class Types(models.TextChoices):
    SOCIAL_ENVIRONMENT = '1'
    PREVENT_CRIME = '2'
    PREVENT_SUICIDE = '3'
    EDUCATIONAL = '4'
    OTHER = '5'


class Neighborhood(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='neighborhood_imam') 
    comment = models.TextField(blank=True)
    participants = models.CharField(max_length=20, choices=Participants.choices)
    types = models.CharField(max_length=20, choices=Types.choices)
    date = models.DateField()
    
    class Meta:
        verbose_name = 'Mahalla '
        verbose_name_plural = 'Mahallalar '

    def __str__(self):
        return self.imam.username