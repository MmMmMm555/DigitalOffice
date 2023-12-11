from django.db import models
from django.core.validators import FileExtensionValidator

from apps.users.models import User, Role
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts

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
    title = models.CharField(max_length=1000)
    direction_type = models.CharField(max_length=11, choices=DirectionTypes.choices, default=DirectionTypes.ORDER)
    file = models.FileField(upload_to='files/direction', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])
    type = models.CharField(max_length=12, choices=Types.choices, default=Types.INFORMATION)
    to_role = models.CharField(max_length=18, choices=Role.choices, default=Role.IMAM)
    to_region = models.ManyToManyField(Regions, related_name='direction')
    to_district = models.ManyToManyField(Districts, related_name='direction', blank=True)
    to_imams = models.ManyToManyField(User, blank=True)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)

    voice = models.BooleanField(default=False)
    image = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    file_bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Buyruq '
        verbose_name_plural = 'Buyruqlar '


class DirectionsEmployeeRead(BaseModel):
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, related_name='directionemployeeread')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directionemployeeread')
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.employee.username

    class Meta:
        verbose_name = 'Buyruq oqilishi '
        verbose_name_plural = 'Buyruq oqilishlari '


class DirectionsEmployeeResult(BaseModel):
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE, related_name='directionemployeeresult')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directionemployeeresult')
    image = models.ImageField(upload_to='images/directionsresult', validators=[FileExtensionValidator(allowed_extensions=['jpg'])], blank=True)
    video = models.FileField(upload_to='videos/directionresult', validators=[FileExtensionValidator(allowed_extensions=['mp4',])], blank=True)
    voice = models.FileField(upload_to='voices/directionresult', validators=[FileExtensionValidator(allowed_extensions=['mp3',])], blank=True)
    comment = models.TextField(blank=True)
    file = models.FileField(upload_to='files/directionresult', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])], blank=True)

    def __str__(self) -> str:
        return self.employee.username

    class Meta:
        verbose_name = 'Buyruq natija '
        verbose_name_plural = 'Buyruq natijalari '
    
