from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Prayers(models.Model):
    label = models.CharField(max_length=255, blank=False)
    name = models.SlugField(max_length=255, blank=False)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"


class PublicPrayers(BaseModel):
    imam = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='imam_prayers')
    prayer = models.ManyToManyField(
        Prayers, related_name='prayers')

    def __str__(self):
        return str(self.id)+": "+self.imam.username+" - "+self.created_at.strftime("%Y-%m-%d")

    class Meta:
        verbose_name = 'Jamoat namozi '
        verbose_name_plural = 'Jamoat namozlari '
