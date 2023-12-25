from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

from apps.users.models import User, Role
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts
from apps.common.validators import validate_file_size
from apps.friday_tesis.models import States


# Create your models here.


class Types(models.TextChoices):
    INFORMATION = '1'
    IMPLEMENT = '2'

class DirectionTypes(models.TextChoices):
    DECISION = '1'
    ORDER = '2'
    PROGRAM = '3'
    MESSAGE = '4'
    MISSION = '5'

class Directions(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name='directions_creator',)
    title = models.CharField(max_length=1000)
    direction_type = models.CharField(max_length=11, choices=DirectionTypes.choices, default=DirectionTypes.ORDER)
    file = models.FileField(upload_to='files/direction', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,], help_text=f"allowed files : {settings.ALLOWED_FILE_TYPES}")
    types = models.CharField(max_length=12, choices=Types.choices, default=Types.INFORMATION)
    
    from_role = models.CharField(max_length=18, choices=Role.choices[:3], default=Role.SUPER_ADMIN)
    to_role = models.CharField(max_length=18, choices=Role.choices[1:], default=Role.IMAM)
    
    to_region = models.ManyToManyField(Regions, related_name='direction')
    to_district = models.ManyToManyField(Districts, related_name='direction', blank=True)
    to_employee = models.ManyToManyField(User, related_name='direction', blank=True)
    
    required_to_region = models.ManyToManyField(Regions, blank=True)
    required_to_district = models.ManyToManyField(Districts, blank=True)
    required_to_employee = models.ManyToManyField(User, blank=True)

    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)

    voice = models.BooleanField(default=False)
    image = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    file_bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.title}"
    
    class Meta:
        ordering = ['-created_at',]
        verbose_name = "Ko'rsatma "
        verbose_name_plural = "Ko'rsatmalar "


class DirectionsEmployeeRead(BaseModel):
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, related_name='directionemployeeread')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directionemployeeread')
    requirement = models.BooleanField(default=False)
    state = models.CharField(max_length=10, choices=States.choices, default=States.UNSEEN)

    def __str__(self) -> str:
        return self.employee.username

    class Meta:
        ordering = ['-created_at',]
        unique_together = ('direction', 'employee',)
        verbose_name = "Ko'rsatma oqilishi "
        verbose_name_plural = "Ko'rsatma oqilishlari "


class ResultImages(BaseModel):
    image = models.ImageField(upload_to='images/direction_result', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True)
    class Meta:
        verbose_name = "Rasm "
        verbose_name_plural = "Rasmlar "

class ResultVideos(BaseModel):
    video = models.FileField(upload_to='videos/direction_result', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_VIDEO_TYPES), validate_file_size,], help_text=f"allowed videos: {settings.ALLOWED_VIDEO_TYPES}", blank=True)
    class Meta:
        verbose_name = "Video "
        verbose_name_plural = "Videolar "

class ResultFiles(BaseModel):
    file = models.FileField(upload_to='files/direction_result', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_FILE_TYPES), validate_file_size,], help_text=f"allowed files: {settings.ALLOWED_FILE_TYPES}", blank=True)
    class Meta:
        verbose_name = "Fayl "
        verbose_name_plural = "Fayllar "

class DirectionsEmployeeResult(BaseModel):
    direction = models.ForeignKey(Directions, on_delete=models.SET_NULL, related_name='direction_employee_result', null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='direction_employee_result')
    voice = models.FileField(upload_to='voices/direction_result', validators=[FileExtensionValidator(allowed_extensions=['mp3',])], help_text=f"allowed images: ['mp3',]", blank=True)
    comment = models.TextField(blank=True)
    images = models.ManyToManyField(ResultImages, blank=True)
    videos = models.ManyToManyField(ResultVideos, blank=True)
    files = models.ManyToManyField(ResultFiles, blank=True)
    
    def __str__(self) -> str:
        return self.employee.username

    class Meta:
        ordering = ['-created_at',]
        unique_together = ('direction', 'employee',)
        verbose_name = "Ko'rsatma natija "
        verbose_name_plural = "Ko'rsatma natijalari "