from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Prayers(models.Model):
    label = models.CharField(verbose_name=_("label"), max_length=255, blank=False)
    name = models.SlugField(verbose_name=_("name"), max_length=255, blank=False)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

    class Meta:
        verbose_name = 'Namoz vaqti '
        verbose_name_plural = 'Namoz vaqtlari '


class PublicPrayers(BaseModel):
    imam = models.ForeignKey(
        User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='imam_prayers')
    prayer = models.ManyToManyField(
        Prayers, verbose_name=_("prayer"), related_name='prayers')

    def __str__(self):
        return str(self.id)+": "+self.imam.username+" - "+self.created_at.strftime("%Y-%m-%d")

    class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Jamoat namozi '
        verbose_name_plural = 'Jamoat namozlari '
