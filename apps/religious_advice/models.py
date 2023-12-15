from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User



class Types(models.TextChoices):
    FIQH = '1'
    CREED = '2'
    OTHER = '3'

class Choices(models.TextChoices):
    PRAYERS = '1'
    SPLEEN = '2'
    COMMERCE = '3'
    DEBT = '4'
    HERITAGE = '5'

    FAITH = '6'
    JIHAD = '7'
    TAKFIR = '8'
    VASIYLA = '9'
    OTHER = '10'


class ReligiousAdvice(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_religious_advice')
    type = models.CharField( max_length=12, choices=Types.choices, default=Types.OTHER, blank=False)
    choices = models.CharField( max_length=12, choices=Choices.choices, blank=False)
    comment = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.imam.username

    class Meta: 
        verbose_name = 'Diniy maslahat '
        verbose_name_plural = 'Diniy maslahatlar '