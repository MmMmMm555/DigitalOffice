from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User
 
# Create your models here.

class Mavlud(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=False)
    comment = models.TextField()
    date = models.DateField()
    
    class Meta:
        verbose_name = 'Mavlud'
        verbose_name_plural = 'Mavludlar'
    
    def __str__(self):
        return self.title