from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User
from apps.charity.models import From, HelpTypes
from apps.common.validators import validate_image_size


class Types(models.TextChoices):
    BUILDING = 'building', _("building")                   # bino
    WATER_DISCHARGE = 'water_discharge', _("water_discharge")     # suv chiqarish
    OTHER = 'other', _("other")                         # boshqa


class Participation(models.TextChoices):
    INITIATIVE = 'initiative', _("initiative")               # tashabbuskor
    PARTICIPANT = 'participant', _("participant")             # ishtirokchi
    OTHER = 'other', _("other")                         # boshqa


class CharityPromotionImages(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/charity_promotion/', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=False)

    class Meta:
        verbose_name = 'Hayriya aksiya rasmi '
        verbose_name_plural = 'Hayriya aksiya rasmilari '

    def __str__(self):
        return self.image.url


class CharityPromotion(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_(
        "imam"), on_delete=models.CASCADE, related_name='imam_charity_promotion')
    types = models.CharField(verbose_name=_(
        "types"), max_length=22, choices=Types.choices, default=Types.BUILDING, blank=False)
    participant = models.CharField(verbose_name=_("participant"), max_length=22,
                                   choices=Participation.choices, default=Participation.INITIATIVE, blank=False)
    help_type = models.CharField(verbose_name=_(
        "help_type"), max_length=22, choices=HelpTypes.choices, blank=False)
    from_who = models.CharField(verbose_name=_(
        "from_who"), max_length=22, choices=From.choices, blank=False)
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    images = models.ManyToManyField(
        CharityPromotionImages, verbose_name=_("images"), blank=True)
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return self.imam

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Hayriya aksiyasi '
        verbose_name_plural = 'Hayriya aksiyalari '
