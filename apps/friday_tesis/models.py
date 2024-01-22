from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.users.models import User
from apps.mosque.models import Mosque
from apps.common.models import BaseModel
from apps.common.validators import validate_file_size, validate_image_size, validate_video_size
from apps.common.regions import Regions, Districts


class States(models.TextChoices):
    UNSEEN = "unseen"
    ACCEPTED = "accepted"
    DONE = "done"
    EXPIRED = "expired"


class ThesisType(models.TextChoices):
    FRIDAY = "friday"
    HAYIT = "hayit"


class FridayThesis(BaseModel):
    title = models.CharField(verbose_name=_("title"), max_length=1000)
    types = models.CharField(verbose_name=_("types"),
                             max_length=6, choices=ThesisType.choices, default=ThesisType.FRIDAY)
    file = models.FileField(verbose_name=_("file"), upload_to='files/fridaytesis', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    file_comment = models.TextField(verbose_name=_(
        "file_comment"), blank=True, null=True)
    attachment = models.FileField(verbose_name=_("attachment"), upload_to='files/attachment', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    attachment_comment = models.TextField(verbose_name=_(
        "attachment_comment"), blank=True, null=True)
    date = models.DateField(verbose_name=_("date"), )
    to_region = models.ManyToManyField(
        Regions, verbose_name=_("to_region"), blank=True)
    to_district = models.ManyToManyField(
        Districts, verbose_name=_("to_district"), blank=True)
    to_mosque = models.ManyToManyField(
        Mosque, verbose_name=_("to_mosque"), blank=True)
    image = models.BooleanField(verbose_name=_("image"), default=False)
    video = models.BooleanField(verbose_name=_("video"), default=False)
    comment = models.BooleanField(verbose_name=_("comment"), default=False)
    file_bool = models.BooleanField(verbose_name=_("file_bool"), default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.title}"

    class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Juma tezisi '
        verbose_name_plural = 'Juma tezislari '


class FridayThesisImamRead(BaseModel):
    tesis = models.ForeignKey(
        FridayThesis, verbose_name=_("tesis"), on_delete=models.CASCADE, related_name='fridaythesisimamread')
    imam = models.ForeignKey(
        User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='fridaythesisimamread')
    requirement = models.BooleanField(
        verbose_name=_("requirement"), default=False)
    state = models.CharField(verbose_name=_("state"),
                             max_length=10, choices=States.choices, default=States.UNSEEN)

    def __str__(self) -> str:
        return f"{self.id}-{self.imam.username} seen:{self.state}  required:{self.requirement}"

    class Meta:
        ordering = ['-created_at',]
        unique_together = ('tesis', 'imam',)
        verbose_name = 'Juma tezisi bildirishnoma '
        verbose_name_plural = 'Juma tezislari bildirishnoma '


class ResultImages(BaseModel):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/tesisresult', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True)


class ResultVideos(BaseModel):
    video = models.FileField(verbose_name=_("video"), upload_to='videos/tesisresult', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_VIDEO_TYPES), validate_video_size,], help_text=f"allowed videos: {settings.ALLOWED_VIDEO_TYPES}", blank=True)


class FridayThesisImamResult(BaseModel):
    tesis = models.ForeignKey(
        FridayThesis, verbose_name=_("tesis"), on_delete=models.CASCADE, related_name='fridaytesisimamresult')
    imam = models.ForeignKey(
        User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='fridaytesisimamresult')
    comment = models.TextField(verbose_name=_(
        "comment"), blank=True, null=True)
    child = models.PositiveIntegerField(verbose_name=_("child"), default=0)
    man = models.PositiveIntegerField(verbose_name=_("man"), default=0)
    old_man = models.PositiveIntegerField(verbose_name=_("old_man"), default=0)
    old = models.PositiveIntegerField(verbose_name=_("old"), default=0)
    file = models.FileField(verbose_name=_("file"), upload_to='files/tesisresult', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,],  help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    images = models.ManyToManyField(
        ResultImages, verbose_name=_("images"), blank=True)
    videos = models.ManyToManyField(
        ResultVideos, verbose_name=_("videos"), blank=True)

    def __str__(self) -> str:
        return self.imam.username

    class Meta:
        ordering = ['-created_at',]
        unique_together = ['tesis', 'imam',]
        verbose_name = 'Juma tezisi imom natija '
        verbose_name_plural = 'Juma tezislari imom natijalar '
