from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Participants(models.TextChoices):
    TEENS = 'teens', _("teens")
    WOMANS = 'womans', _("womans")
    MANS = 'mans', _("mans")
    OLDER_MAN = 'older_man', _("older_man")
    MIX = 'mix', _("mix")


class Types(models.TextChoices):
    SOCIAL_ENVIRONMENT = 'social_environment', _("social_environment")
    PREVENT_CRIME = 'prevent_crime', _("prevent_crime")
    PREVENT_SUICIDE = 'prevent_suicide', _("prevent_suicide")
    EDUCATIONAL = 'educational', _("educational")
    OTHER = 'other', _("other")


class Neighborhood(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_(
        "imam"), on_delete=models.CASCADE, related_name='neighborhood_imam')
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    participants = models.CharField(verbose_name=_(
        "participants"), max_length=20, choices=Participants.choices, blank=False)
    types = models.CharField(verbose_name=_(
        "types"), max_length=20, choices=Types.choices, blank=False)
    date = models.DateField(verbose_name=_("date"), )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Mahalla '
        verbose_name_plural = 'Mahallalar '

    def __str__(self):
        return self.imam.username
