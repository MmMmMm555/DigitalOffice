from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from apps.common.models import BaseModel
from apps.users.models import User


class Types(models.TextChoices):
    INVALID = '1'
    POOR = '2'
    NONE_BREADWINNER = '3'
    STUDENT = '4'
    OTHER = '5'

class HelpTypes(models.TextChoices):
    MONEY = '1'
    FOOD = '2'
    CLOSES = '3'
    MEDICINE = '4'
    OTHER = '5'

class From(models.TextChoices):
    MOSQUE = '1'
    SPONSOR = '2'
    ZAKAT = '3'
    FIDYA = '4'
    FITR = '5'
    OTHER = '6'


class Images(models.Model):
    image = models.ImageField(upload_to='images/charity/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=False)

    class Meta:
        verbose_name = 'Hayriya rasmi '
        verbose_name_plural = 'Hayriya rasmilari '
    
    def __str__(self):
        return f"{self.id}-{self.image.url}"

class Charity(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_charity')
    types = models.CharField(max_length=22, choices=Types.choices, default=Types.POOR, blank=False)
    help_type = models.CharField(max_length=22, choices=HelpTypes.choices, blank=False)
    from_who = models.CharField(max_length=22, choices=From.choices, blank=False)
    summa = models.FloatField(blank=False, default=0)
    images = models.ManyToManyField(Images, blank=True)
    comment = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.imam.username

    class Meta: 
        verbose_name = 'Hayriya '
        verbose_name_plural = 'Hayriyalar '