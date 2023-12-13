from django.db import models
from apps.common.models import BaseModel
from django.conf import settings
from django.core.validators import FileExtensionValidator
from apps.users.models import User
 
# Create your models here.


class Wedding(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wedding')
    date = models.DateField()
    fhdyo_file = models.FileField(upload_to='files/wedding_fhdyo', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}")
    wedding_document = models.FileField(upload_to='files/wedding_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}")
    mahir = models.FloatField(default=0)
    comment = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Nikoh '
        verbose_name_plural = 'Nikohlar '
    
    def __str__(self):
        return f"{self.id}: {self.imam} - {self.date}"