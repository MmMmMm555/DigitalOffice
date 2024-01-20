from django.db import models
from django.utils.translation import gettext_lazy as _


class Regions(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self) -> str:
        return self.name


class Districts(models.Model):
    name = models.CharField(_("name"), max_length=100)
    region = models.ForeignKey(Regions, verbose_name=_(
        "region"), on_delete=models.CASCADE, related_name='district')

    def __str__(self) -> str:
        return self.name
