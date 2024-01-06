from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class CeremonyTypes(models.TextChoices):
    FUNERAL = '1' # janoza
    MOURNING = '2' # aza


class Ceremony(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=300, blank=False)
    comment = models.TextField(blank=True, null=True)
    types = models.CharField(max_length=15, choices=CeremonyTypes.choices, default=CeremonyTypes.FUNERAL)
    date = models.DateField()

    class Meta:
        verbose_name = "Marosim "
        verbose_name_plural = "Marosimlar "
    
    def __str__(self):
        return self.title