from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User
from django.utils.translation import gettext_lazy as _


class CeremonyTypes(models.TextChoices):
    FUNERAL = 'funeral'   # janaza
    MOURNING = 'mourning' # aza


class Ceremony(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_("imam"), on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(verbose_name=_("title"), max_length=300, blank=False)
    comment = models.TextField(verbose_name=_("comment"), blank=True, null=True)
    types = models.CharField(verbose_name=_("types"), max_length=15, choices=CeremonyTypes.choices, default=CeremonyTypes.FUNERAL)
    date = models.DateField(verbose_name=_("date"), )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Marosim "
        verbose_name_plural = "Marosimlar "

    def __str__(self):
        return self.title