from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User
from apps.common.validators import validate_image_size


class Types(models.TextChoices):
    INVALID = 'invalid'                    # nogiron
    POOR = 'poor'                          # kambag'al
    NONE_BREADWINNER = 'none_breadwinner'  # boquvchisiz
    STUDENT = 'student'                    # talaba
    OTHER = 'other'                        # boshqa

class HelpTypes(models.TextChoices):
    MONEY = 'money'               #  pul
    FOOD = 'food'                 #  ovqat
    CLOSES = 'closes'             #  kiyim
    MEDICINE = 'medicine'         #  dori
    OTHER = 'other'               #  boshqa

class From(models.TextChoices):
    MOSQUE = 'mosque'             #  masjid
    SPONSOR = 'sponsor'           #  sponsor
    ZAKAT = 'zakat'               #  zakot
    FIDYA = 'fidya'               #  fidya
    FITR = 'fitr'                 #  fitr
    OTHER = 'other'               #  bsohqa


class Images(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/charity/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=False)

    class Meta:
        verbose_name = 'Hayriya rasmi '
        verbose_name_plural = 'Hayriya rasmilari '
    
    def __str__(self):
        return self.image.url


class Charity(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='imam_charity')
    types = models.CharField(verbose_name=_("types"), max_length=22, choices=Types.choices, default=Types.POOR, blank=False)
    help_type = models.CharField(verbose_name=_("help_type"), max_length=22, choices=HelpTypes.choices, blank=False)
    from_who = models.CharField(verbose_name=_("from_who"), max_length=22, choices=From.choices, blank=False)
    summa = models.FloatField(verbose_name=_("summa"), blank=False, default=0)
    images = models.ManyToManyField(Images, verbose_name=_("images"), blank=True)
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return self.imam

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Hayriya '
        verbose_name_plural = 'Hayriyalar '