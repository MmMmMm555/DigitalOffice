from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from .manager import UserManager

from apps.employee.models import Employee
from apps.common.regions import Regions, Districts


class Role(models.TextChoices):
    SUPER_ADMIN = '1', _("super_admin")
    REGION_ADMIN = '2', _("region_admin")
    DISTRICT_ADMIN = '3', _("district_admin")
    IMAM = '4', _("imam")
    SUB_IMAM = '5', _("sub_imam")


class User(AbstractUser):
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    region = models.ForeignKey(
        Regions, verbose_name=_("region"), on_delete=models.SET_NULL, blank=True, null=True, related_name='region')
    district = models.ForeignKey(
        Districts, verbose_name=_("district"), on_delete=models.SET_NULL, blank=True, null=True, related_name='district')
    profil = models.OneToOneField(Employee, unique=True, verbose_name=_(
        "profile"), on_delete=models.SET_NULL, related_name='profile', blank=True, null=True)
    role = models.CharField(verbose_name=_("role"),
                            max_length=18, choices=Role.choices, default=Role.IMAM, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['-id']
