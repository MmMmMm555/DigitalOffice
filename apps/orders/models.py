from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from apps.users.models import User, Role
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts
from apps.common.validators import validate_file_size, validate_image_size, validate_video_size
from apps.friday_tesis.models import States
from apps.mosque.models import Mosque


# Create your models here.


class ToRole(models.TextChoices):
    REGION_ADMIN = u'2'
    DISTRICT_ADMIN = u'3'
    IMAM = u'4'
    SUB_IMAM = u'5'


class Types(models.TextChoices):
    INFORMATION = 'information'
    IMPLEMENT = 'implement'


class DirectionTypes(models.TextChoices):
    DECISION = 'decision'
    ORDER = 'order'
    PROGRAM = 'program'
    MESSAGE = 'message'
    MISSION = 'mission'


class DirectionFiles(BaseModel):
    file = models.FileField(verbose_name=_("file"), upload_to='files/direction', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,], help_text=f"allowed files : {settings.ALLOWED_FILE_TYPES}")

    class Meta:
        verbose_name = "Fayl "
        verbose_name_plural = "Fayllar "


class Directions(BaseModel):
    creator = models.ForeignKey(User, verbose_name=_("creator"), on_delete=models.SET_NULL,
                                null=True, blank=False, related_name='directions_creator',)
    title = models.CharField(verbose_name=_("title"), max_length=1000)
    direction_type = models.CharField(verbose_name=_("direction_type"),
                                      max_length=11, choices=DirectionTypes.choices, default=DirectionTypes.ORDER)
    file = models.ManyToManyField(
        DirectionFiles, verbose_name=_("file"), blank=True)
    comments = models.TextField(verbose_name=_("comments"), blank=True)
    types = models.CharField(verbose_name=_("types"),
                             max_length=12, choices=Types.choices, default=Types.INFORMATION)

    from_role = models.CharField(verbose_name=_("from_role"),
                                 max_length=18, choices=Role.choices[:3], default=Role.SUPER_ADMIN)
    to_role = ArrayField(models.CharField(verbose_name=_("to_role"),
                                          max_length=18, choices=ToRole.choices, default=ToRole.IMAM, blank=True, null=True), default=list, blank=True)

    to_region = models.ManyToManyField(Regions, verbose_name=_(
        "to_region"), related_name='direction', blank=True)
    to_district = models.ManyToManyField(
        Districts, verbose_name=_("to_district"), related_name='direction', blank=True)
    to_employee = models.ManyToManyField(
        Mosque, verbose_name=_("to_employee"), related_name='direction', blank=True)

    required_to_region = models.ManyToManyField(
        Regions, verbose_name=_("required_to_region"), blank=True)
    required_to_district = models.ManyToManyField(
        Districts, verbose_name=_("required_to_district"), blank=True)
    required_to_employee = models.ManyToManyField(
        Mosque, verbose_name=_("required_to_employee"), blank=True)

    from_date = models.DateField(verbose_name=_("from_date"), blank=False)
    to_date = models.DateField(verbose_name=_(
        "to_date"), blank=True, null=True,)

    voice = models.BooleanField(verbose_name=_("voice"), default=False)
    image = models.BooleanField(verbose_name=_("image"), default=False)
    video = models.BooleanField(verbose_name=_("video"), default=False)
    comment = models.BooleanField(verbose_name=_("comment"), default=False)
    file_bool = models.BooleanField(verbose_name=_("file_bool"), default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.title}"

    class Meta:
        ordering = ['-created_at',]
        verbose_name = "Ko'rsatma "
        verbose_name_plural = "Ko'rsatmalar "


class DirectionsEmployeeRead(BaseModel):
    direction = models.ForeignKey(
        Directions, verbose_name=_("direction"), on_delete=models.CASCADE, related_name='directionemployeeread')
    employee = models.ForeignKey(
        User, verbose_name=_("employee"), on_delete=models.CASCADE, related_name='directionemployeeread')
    requirement = models.BooleanField(
        verbose_name=_("requirement"), default=False)
    state = models.CharField(verbose_name=_("state"),
                             max_length=10, choices=States.choices, default=States.UNSEEN)

    def __str__(self) -> str:
        return self.employee.username

    class Meta:
        ordering = ['-created_at',]
        unique_together = ('direction', 'employee',)
        verbose_name = "Ko'rsatma oqilishi "
        verbose_name_plural = "Ko'rsatma oqilishlari "


class ResultImages(BaseModel):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/direction_result', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True)

    class Meta:
        verbose_name = "Rasm "
        verbose_name_plural = "Rasmlar "


class ResultVideos(BaseModel):
    video = models.FileField(verbose_name=_("video"), upload_to='videos/direction_result', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_VIDEO_TYPES), validate_video_size,], help_text=f"allowed videos: {settings.ALLOWED_VIDEO_TYPES}", blank=True)

    class Meta:
        verbose_name = "Video "
        verbose_name_plural = "Videolar "


class ResultFiles(BaseModel):
    file = models.FileField(verbose_name=_("file"), upload_to='files/direction_result', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)

    class Meta:
        verbose_name = "Fayl "
        verbose_name_plural = "Fayllar "


class DirectionsEmployeeResult(BaseModel):
    direction = models.ForeignKey(
        Directions, verbose_name=_("direction"), on_delete=models.SET_NULL, related_name='direction_employee_result', null=True)
    employee = models.ForeignKey(
        User, verbose_name=_("employee"), on_delete=models.CASCADE, related_name='direction_employee_result')
    voice = models.FileField(verbose_name=_("voice"), upload_to='voices/direction_result', validators=[FileExtensionValidator(
        allowed_extensions=['mp3',]), validate_file_size], help_text=f"allowed voices: ['mp3',]", blank=True)
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    images = models.ManyToManyField(
        ResultImages, verbose_name=_("images"), blank=True)
    videos = models.ManyToManyField(
        ResultVideos, verbose_name=_("videos"), blank=True)
    files = models.ManyToManyField(
        ResultFiles, verbose_name=_("files"), blank=True)

    def __str__(self) -> str:
        return self.employee.username

    class Meta:
        ordering = ['-created_at',]
        unique_together = ('direction', 'employee',)
        verbose_name = "Ko'rsatma natija "
        verbose_name_plural = "Ko'rsatma natijalari "
