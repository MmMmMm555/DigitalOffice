from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from apps.common.models import BaseModel
from apps.users.models import User
from apps.charity.models import From, HelpTypes


class Types(models.TextChoices):
    BUILDING = '1'
    WATER_DISCHARGE = '2'
    OTHER = '3'

class Participation(models.TextChoices):
    INITIATIVE = '1'
    PARTICIPANT = '2'
    OTHER = '3'


class CharityPromotionImages(models.Model):
    image = models.ImageField(upload_to='images/charity_promotion/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=False)

    class Meta:
        verbose_name = 'Hayriya aksiya rasmi '
        verbose_name_plural = 'Hayriya aksiya rasmilari '
    
    def __str__(self):
        return self.image.url


class CharityPromotion(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_charity_promotion')
    types = models.CharField(max_length=22, choices=Types.choices, default=Types.BUILDING, blank=False)
    participant = models.CharField(max_length=22, choices=Participation.choices, default=Participation.INITIATIVE, blank=False)
    help_type = models.CharField(max_length=22, choices=HelpTypes.choices, blank=False)
    from_who = models.CharField(max_length=22, choices=From.choices, blank=False)
    comment = models.TextField()
    images = models.ManyToManyField(CharityPromotionImages, blank=True)
    date = models.DateField()
    
    def __str__(self):
        return self.imam.username

    class Meta: 
        verbose_name = 'Hayriya aksiyasi '
        verbose_name_plural = 'Hayriya aksiyalari '