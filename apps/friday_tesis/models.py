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

    image = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    file_bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.title}"

    class Meta:
        verbose_name = 'Juma tezisi '
        verbose_name_plural = 'Juma tezislari '


class FridayTesisImamRead(BaseModel):
    tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='fridaytesisimamread')
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridaytesisimamread')
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}-{self.imam.username} {self.seen}"

    class Meta:
        verbose_name = 'Juma tezisi imom oqigan '
        verbose_name_plural = 'Juma tezislari imom oqiganlar '


class FridayTesisImamResult(BaseModel):
    tesis = models.ForeignKey(FridayTesis, on_delete=models.CASCADE, related_name='fridaytesisimamresult')
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridaytesisimamresult')
    image = models.ImageField(upload_to='images/tesisresult', validators=[FileExtensionValidator(allowed_extensions=['jpg'])], blank=True)
    video = models.FileField(upload_to='videos/tesisresult', validators=[FileExtensionValidator(allowed_extensions=['mp4',])], blank=True)
    comment = models.TextField(blank=True)
    file = models.FileField(upload_to='files/tesisresult', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])], blank=True)

    def __str__(self) -> str:
        return self.imam.username

    class Meta:
        verbose_name = 'Juma tezisi imom natija '
        verbose_name_plural = 'Juma tezislari imom natijalar '