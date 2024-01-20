from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from apps.common.validators import validate_file_size, validate_image_size
from apps.common.models import BaseModel
from apps.users.models import User


class Death(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='death')
    date = models.DateField(verbose_name=_("date"), )
    image = models.ImageField(verbose_name=_("image"), upload_to='images/death_images', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    file = models.FileField(verbose_name=_("file"), upload_to='files/death_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    comment = models.TextField(verbose_name=_("comment"), blank=True, null=True)
    
    class Meta:
        verbose_name = "O'lim "
        verbose_name_plural = "O'limlar "
    
    def __str__(self):
        return f"{self.id}: {self.imam} : {self.date}"