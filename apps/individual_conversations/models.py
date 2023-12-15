from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from apps.common.models import BaseModel
from apps.users.models import User



class Types(models.TextChoices):
    NEED_SOCIAL_ASSISTANCE = '1'
    PRONE_TO_CRIME = '2'
    OTHER = '3'


class IndividualConversation(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_individual_conversation')
    type = models.CharField( max_length=22, choices=Types.choices, default=Types.NEED_SOCIAL_ASSISTANCE, blank=False)
    title = models.CharField(max_length=300)
    comment = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Saxsiy suhbat '
        verbose_name_plural = 'Saxsiy suhbatlar '

class Images(models.Model):
    conversation = models.ForeignKey(IndividualConversation, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/conversation_images/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    
    class Meta: 
        verbose_name = 'Suhbat rasmi '
        verbose_name_plural = 'Suhbat rasmlari '