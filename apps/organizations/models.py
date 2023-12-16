from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User

# Create your models here.


class OrganizationType(models.TextChoices):
    EDUCATIONAL_INSTITUTION = '1'
    PRISON = '2'
    MILITARY_UNIT = '3'
    OTHER = '4'

class InstitutionType(models.TextChoices):
    HIGH = '1'
    MIDDLE = '2'
    GENERAL = '3'

class PrisonerType(models.TextChoices):
    LAW_159 = '1'
    LAW_244 = '2'
    YOUNG = '3'
    MINOR = '4'
    OTHER = '5'

class ParticipantType(models.TextChoices):
    EMPLOYEE = '1'
    STUDENT = '2'
    SCHOOL_STUDENT = '3'
    OTHER = '4'
    

class Organization(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization')
    type = models.CharField(max_length=18, choices=OrganizationType.choices)
    institution_type = models.CharField(max_length=10, choices=InstitutionType.choices, blank=True, null=True)
    participant_type = models.CharField(max_length=14, choices=ParticipantType.choices, blank=True, null=True)
    prisoner_type = models.CharField(max_length=10, choices=PrisonerType.choices, blank=True, null=True)        
    description = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.imam.username} {self.type}"

    class Meta:
        verbose_name = 'Tashkilot '
        verbose_name_plural = 'Tashkilotlar '