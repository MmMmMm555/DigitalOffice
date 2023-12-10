from django.db import models
from django.core.validators import FileExtensionValidator

from apps.users.models import User
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts

# Create your models here.


class FridayTesis(BaseModel):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/fridaytesis', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])
    attachment = models.FileField(upload_to='files/attachment', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])], blank=True)
    to_region = models.ManyToManyField(Regions)
    to_district = models.ManyToManyField(Districts, blank=True)
    to_imams = models.ManyToManyField(User, blank=True)
    date = models.DateField()
    
    empty = models.BooleanField(default=False)
    image = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    file_bool = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Juma tezisi '
        verbose_name_plural = 'Juma tezislari '


class FridayTesisImamRead(models.Model):
    tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='fridaytesisimamread')
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridaytesisimamread')
    seen = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.imam.username
