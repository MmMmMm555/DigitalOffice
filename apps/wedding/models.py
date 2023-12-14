from django.db import models
from apps.common.models import BaseModel
from apps.users.models import User


class WeddingTypes(models.TextChoices):
    MARRIAGE = '1'
    AQEEQAH_SUNANT = '2'
    HAMD = '3'


class Wedding(BaseModel):
    title = models.CharField(max_length=300, blank=False)
    comment = models.TextField(blank=True, null=True)
    imam = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    types = models.CharField(max_length=15, choices=WeddingTypes.choices, default=WeddingTypes.MARRIAGE)
    date = models.DateField()
    
    class Meta:
        verbose_name = "To'y "
        verbose_name_plural = "To'ylar "
    
    def __str__(self):
        return self.title
    
