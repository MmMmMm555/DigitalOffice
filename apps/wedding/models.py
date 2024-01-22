from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class WeddingTypes(models.TextChoices):
    MARRIAGE = 'marriage'
    AQEEQAH_SUNANT = 'aqeeqah_sunant'
    HAMD = 'hamd'


class Wedding(BaseModel):
    title = models.CharField(verbose_name=_(
        "title"), max_length=300, blank=False)
    comment = models.TextField(verbose_name=_(
        "comment"), blank=True, null=True)
    imam = models.ForeignKey(User, verbose_name=_(
        "imam"), on_delete=models.SET_NULL, null=True, blank=False)
    types = models.CharField(verbose_name=_(
        "types"), max_length=15, choices=WeddingTypes.choices, default=WeddingTypes.MARRIAGE)
    date = models.DateField(verbose_name=_("date"), )

    class Meta:
        verbose_name = "To'y "
        verbose_name_plural = "To'ylar "

    def __str__(self):
        return self.title
