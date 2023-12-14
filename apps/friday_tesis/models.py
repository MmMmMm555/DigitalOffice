from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

from apps.users.models import User
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts


# Create your models here.


class States(models.TextChoices):
    UNSEEN = 1
    ACCEPTED = 2
    DONE = 3

class FridayTesis(BaseModel):
    title = models.CharField(max_length=1000)
    # title_slug = models.SlugField(max_length=1000)
    file = models.FileField(upload_to='files/fridaytesis', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}")
    attachment = models.FileField(upload_to='files/attachment', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    date = models.DateField()
    to_region = models.ManyToManyField(Regions, blank=True)
    to_district = models.ManyToManyField(Districts, blank=True)
    to_imams = models.ManyToManyField(User, blank=True)
    image = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    file_bool = models.BooleanField(default=False)
   

    def __str__(self) -> str:
        return f"{self.id}-{self.title}"

    class Meta:
        verbose_name = 'Juma tezisi '
        verbose_name_plural = 'Juma tezislari '


# class FridayTesisRequireds(BaseModel):
#     tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='tesisrequireds')
#     to_region = models.ManyToManyField(Regions)
#     to_district = models.ManyToManyField(Districts, blank=True)
#     to_imams = models.ManyToManyField(User, blank=True)
#     image = models.BooleanField(default=False)
#     video = models.BooleanField(default=False)
#     comment = models.BooleanField(default=False)
#     file_bool = models.BooleanField(default=False)


class FridayTesisImamRead(BaseModel):
    tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='fridaytesisimamread')
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridaytesisimamread')
    seen = models.BooleanField(default=False)
    requirement = models.BooleanField(default=False)
    state = models.CharField(max_length=10, choices=States.choices, default=States.UNSEEN)
    def __str__(self) -> str:
        return f"{self.id}-{self.imam.username} {self.seen}"

    class Meta:
        verbose_name = 'Juma tezisi imom oqigan '
        verbose_name_plural = 'Juma tezislari imom oqiganlar '


class FridayTesisImamResult(BaseModel):
    tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='fridaytesisimamresult')
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridaytesisimamresult')
    comment = models.TextField(blank=True)
    file = models.FileField(upload_to='files/tesisresult', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES)],  help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)

    def __str__(self) -> str:
        return self.imam.username

    class Meta:
        verbose_name = 'Juma tezisi imom natija '
        verbose_name_plural = 'Juma tezislari imom natijalar '


class ResultImages(BaseModel):
    result = models.ForeignKey(FridayTesisImamResult, on_delete=models.CASCADE, verbose_name='result_image')
    image = models.ImageField(upload_to='images/tesisresult', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True)

class ResultVideos(BaseModel):
    result = models.ForeignKey(FridayTesisImamResult, on_delete=models.CASCADE, verbose_name='result_video')
    video = models.FileField(upload_to='videos/tesisresult', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_VIDEO_TYPES)], help_text=f"allowed videos: {settings.ALLOWED_VIDEO_TYPES}", blank=True)