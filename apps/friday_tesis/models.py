from django.db import models
from django.core.validators import FileExtensionValidator

from apps.users.models import User
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts

# Create your models here.


class FridayTesis(BaseModel):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/fridaytesis', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt'])])
    attachment = models.FileField(upload_to='files/attachment', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt'])], blank=True)
    to_region = models.ManyToManyField(Regions)
    to_district = models.ManyToManyField(Districts, blank=True)
    to_imams = models.ManyToManyField(User, blank=True)
    date = models.DateField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Juma tezisi '
        verbose_name_plural = 'Juma tezislari '


class FridayTesisReqiredFields(models.Model):
    tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='requiredfields')
    to_region = models.ManyToManyField(Regions, blank=True)
    to_district = models.ManyToManyField(Districts, blank=True)
    to_imams = models.ManyToManyField(User, blank=True)
    empty = models.BooleanField(default=False)
    image = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    file = models.BooleanField(default=False)