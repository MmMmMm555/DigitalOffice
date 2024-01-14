from django.db import models
from apps.common.models import BaseModel
from django.conf import settings
from django.core.validators import FileExtensionValidator
from apps.users.models import User
 
# Create your models here.


class Marriage(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marriage')
    date = models.DateField()
    marriage_image = models.FileField(upload_to='image/marriage_images', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    marriage_document = models.FileField(upload_to='files/marriage_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    fhdyo_document = models.FileField(upload_to='files/fhdyo_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    fhdyo_image = models.FileField(upload_to='images/fhdyo_images', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    mahr = models.FloatField(default=0)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Nikoh '
        verbose_name_plural = 'Nikohlar '
    
    def __str__(self):
        return f"{self.id}: {self.imam} - {self.date}"