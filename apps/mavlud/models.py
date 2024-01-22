from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Mavlud(BaseModel):
    imam = models.ForeignKey(User, verbose_name=_(
        "imam"), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_(
        "title"), max_length=300, blank=False)
    comment = models.TextField(verbose_name=_("comment"), )
    date = models.DateField(verbose_name=_("date"), )

    class Meta:
        verbose_name = 'Mavlud'
        verbose_name_plural = 'Mavludlar'

    def __str__(self):
        return self.title
