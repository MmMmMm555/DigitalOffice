from django.db import models
from django.utils.translation import gettext_lazy as _


class Regions(models.Model):
    name = models.CharField(_("nomi"), max_length=100)

    def __str__(self) -> str:
        return self.name

class Districts(models.Model):
    name = models.CharField(_("nomi"), max_length=100)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, related_name='district')
    
    def __str__(self) -> str:
        return self.name