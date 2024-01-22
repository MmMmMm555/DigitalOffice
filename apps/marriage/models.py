from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User
from apps.common.validators import validate_file_size, validate_image_size


class Marriage(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='marriage')
    date = models.DateField(verbose_name=_("date"), )
    marriage_image = models.FileField(verbose_name=_("marriage_image"), upload_to='image/marriage_images', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    marriage_document = models.FileField(verbose_name=_("marriage_document"), upload_to='files/marriage_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    fhdyo_document = models.FileField(verbose_name=_("fhdyo_document"), upload_to='files/fhdyo_docs', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    fhdyo_image = models.FileField(verbose_name=_("fhdyo_image"), upload_to='images/fhdyo_images', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    mahr = models.FloatField(verbose_name=_("mahr"), default=0)
    comment = models.TextField(verbose_name=_("comment"), blank=True, null=True)

    class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Nikoh '
        verbose_name_plural = 'Nikohlar '

    def __str__(self):
        return f"{self.id}: {self.imam}"