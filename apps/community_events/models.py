from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from apps.common.models import BaseModel
from apps.users.models import User



class Types(models.TextChoices):
    HOLIDAY = '1'
    HASHAR = '2'
    OPENING_CEREMONY = '3'
    OTHER = '4'


class Images(models.Model):
    image = models.ImageField(upload_to='images/community_event/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    class Meta: 
        verbose_name = 'Jamoat tadbiri rasmi '
        verbose_name_plural = 'Jamoat tadbirlari rasmi '


class CommunityEvents(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_community_events')
    type = models.CharField(max_length=22, choices=Types.choices, default=Types.HOLIDAY, blank=False)
    comment = models.TextField()
    images = models.ManyToManyField(Images, blank=True)
    date = models.DateField()
    
    def __str__(self):
        return self.imam.username

    class Meta: 
        verbose_name = 'Jamoat tadbiri '
        verbose_name_plural = 'Jamoat tadbirlari '