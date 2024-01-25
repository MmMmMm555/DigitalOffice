from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User
from apps.common.validators import validate_image_size


class Types(models.TextChoices):
    NEED_SOCIAL_ASSISTANCE = 'need_social_assistance'
    PRONE_TO_CRIME = 'prone_to_crime'
    OTHER = 'other'


class IndividualConversationImages(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/conversation_images/', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    def __str__(self) -> str:
        return self.image.url

    class Meta:
        verbose_name = 'Suhbat rasmi '
        verbose_name_plural = 'Suhbat rasmlari '


class IndividualConversation(BaseModel):
    imam = models.ForeignKey(
        User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='imam_individual_conversation')
    images = models.ManyToManyField(IndividualConversationImages, verbose_name=_("images"), blank=False,)
    types = models.CharField(verbose_name=_("types"), max_length=22, choices=Types.choices,
                            default=Types.NEED_SOCIAL_ASSISTANCE, blank=False)
    title = models.CharField(verbose_name=_("title"), max_length=300)
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Saxsiy suhbat '
        verbose_name_plural = 'Saxsiy suhbatlar '