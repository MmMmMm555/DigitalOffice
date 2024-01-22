from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Types(models.TextChoices):
    FIQH = 'fiqh'
    CREED = 'creed'
    OTHER = 'other'


class Choices(models.TextChoices):
    PRAYERS = 'prayers'
    SPLEEN = 'spleen'
    COMMERCE = 'commerce'
    DEBT = 'debt'
    HERITAGE = 'heritage'

    FAITH = 'faith'
    JIHAD = 'jihad'
    TAKFIR = 'takfir'
    VASIYLA = 'vasiyla'
    OTHER = 'other0'


class ReligiousAdvice(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_(
        "imam"), on_delete=models.CASCADE, related_name='imam_religious_advice')
    type = models.CharField(verbose_name=_(
        "type"), max_length=12, choices=Types.choices, default=Types.OTHER, blank=False)
    choices = models.CharField(verbose_name=_(
        "choices"), max_length=12, choices=Choices.choices, blank=False)
    comment = models.TextField(verbose_name=_("comment"), )
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return self.imam.username

    class Meta:
        verbose_name = 'Diniy maslahat '
        verbose_name_plural = 'Diniy maslahatlar '
