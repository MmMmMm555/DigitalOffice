from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class OrganizationType(models.TextChoices):
    EDUCATIONAL_INSTITUTION = 'educational_institution'
    PRISON = 'prison'
    MILITARY_UNIT = 'military_unit'
    OTHER = 'other'


class InstitutionType(models.TextChoices):
    HIGH = 'high'
    MIDDLE = 'middle'
    GENERAL = 'general'


class PrisonerType(models.TextChoices):
    LAW_159 = 'law_159'
    LAW_244 = 'law_244'
    YOUNG = 'young'
    MINOR = 'minor'     # kichik
    OTHER = 'other'


class ParticipantType(models.TextChoices):
    EMPLOYEE = 'employee'
    STUDENT = 'student'
    SCHOOL_STUDENT = 'school_student'
    OTHER = 'other'


class Organization(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_(
        "imam"), on_delete=models.CASCADE, related_name='organization')
    type = models.CharField(verbose_name=_(
        "type"), max_length=23, choices=OrganizationType.choices)
    institution_type = models.CharField(verbose_name=_(
        "institution_type"), max_length=10, choices=InstitutionType.choices, blank=True, null=True)
    participant_type = models.CharField(verbose_name=_(
        "participant_type"), max_length=14, choices=ParticipantType.choices, blank=True, null=True)
    prisoner_type = models.CharField(verbose_name=_(
        "prisoner_type"), max_length=10, choices=PrisonerType.choices, blank=True, null=True)
    description = models.TextField(verbose_name=_(
        "description"), null=True, blank=True)
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return f"{self.imam.username} {self.type}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tashkilot '
        verbose_name_plural = 'Tashkilotlar '
