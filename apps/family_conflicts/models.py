from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Causes(models.TextChoices):
    PROPERTY = 'property'
    HERITAGE = 'heritage'
    JEALOUSY = 'jealousy'
    NOT_UNDERSTANDING = 'not_understanding'
    OTHER = 'other'

class Types(models.TextChoices):
    BROTHERS = 'brothers'
    COUPLE = 'couple'
    PARENT_AND_CHILD = 'parent_and_child'

class Result(models.TextChoices):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    ABSTRACT = 'abstract'


class FamilyConflict(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='family_conflicts_imam') 
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    causes = models.CharField(verbose_name=_("causes"), max_length=20, choices=Causes.choices, blank=False)
    types = models.CharField(verbose_name=_("types"), max_length=20, choices=Types.choices, blank=False)
    results = models.CharField(verbose_name=_("results"), max_length=20, choices=Result.choices, blank=False)
    date = models.DateField(verbose_name=_("date"), )
    
    class Meta:
        verbose_name = 'Oilaviy muammo '
        verbose_name_plural = 'Oilaviy muammolar '

    def __str__(self):
        return self.imam