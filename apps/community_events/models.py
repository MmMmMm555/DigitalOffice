from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from apps.common.validators import validate_image_size
from apps.common.models import BaseModel
from apps.users.models import User


class Types(models.TextChoices):
    HOLIDAY = 'holiday'                   # tug'ilgan kun
    HASHAR = 'hashar'                     # hashar
    OPENING_CEREMONY = 'opening_ceremony' # ochilish marosimi
    OTHER = 'other'                       # boshqa


class Images(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/community_event/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    
    def __str__(self) -> str:
        return self.image.url
    
    class Meta: 
        verbose_name = 'Jamoat tadbiri rasmi '
        verbose_name_plural = 'Jamoat tadbirlari rasmi '


class CommunityEvents(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='imam_community_events')
    types = models.CharField(verbose_name=_("types"), max_length=22, choices=Types.choices, default=Types.HOLIDAY, blank=False)
    comment = models.TextField(verbose_name=_("comment"), blank=True,)
    images = models.ManyToManyField(Images, verbose_name=_("images"), blank=True)
    date = models.DateField(verbose_name=_("date"), )
    
    def __str__(self):
        return self.imam.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Jamoat tadbiri '
        verbose_name_plural = 'Jamoat tadbirlari '