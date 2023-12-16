from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Prayers(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self) -> str:
        return self.name

class PublicPrayers(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_prayers')
    prayer = models.ForeignKey(Prayers, on_delete=models.SET_NULL, related_name='prayers', null=True)

    def __str__(self):
        return str(self.id)+": "+self.imam.username+" - "+self.prayer.name+" - "+self.created_at.strftime("%Y-%m-%d")

    class Meta:
        verbose_name = 'Jamoat namozi '
        verbose_name_plural = 'Jamoat namozlari '