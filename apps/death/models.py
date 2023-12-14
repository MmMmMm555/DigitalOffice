from django.db import models
from apps.common.models import BaseModel
from django.conf import settings
from django.core.validators import FileExtensionValidator
from apps.users.models import User
 
# Create your models here.


class Death(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='death')
    date = models.DateField()
    image = models.ImageField(upload_to='files/death_images', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    file = models.FileField(upload_to='files/death_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    comment = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "O'lim "
        verbose_name_plural = "O'limlar "
    
    def __str__(self):
        return f"{self.id}: {self.imam} - {self.date}"