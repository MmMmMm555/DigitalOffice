from django.db import models
from django.core.validators import FileExtensionValidator

from apps.users.models import User, Role
from apps.common.models import BaseModel
from apps.common.regions import Regions, Districts

# Create your models here.


class OrderTypes(models.TextChoices):
    INFORMATION = '1'
    IMPLEMENT = '2'

class Orders(BaseModel):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/orders', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])
    type = models.CharField(max_length=12, choices=OrderTypes.choices, default=OrderTypes.INFORMATION)
    to_role = models.CharField(max_length=18, choices=Role.choices, default=Role.IMAM)
    to_region = models.ManyToManyField(Regions, related_name='orders')
    to_district = models.ManyToManyField(Districts, related_name='orders', blank=True)
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


class OrdersImamResult(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='orderimamread')
    employee = models.ForeignKey(User.objects.filter(role__in=['4', '2', '3']), on_delete=models.CASCADE, related_name='orderemployeeread')
    seen = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/ordersresult', validators=[FileExtensionValidator(allowed_extensions=['jpg'])], blank=True)
    video = models.FileField(upload_to='videos/ordersresult', validators=[FileExtensionValidator(allowed_extensions=['mp4',])], blank=True)
    voice = models.FileField(upload_to='voices/ordersresult', validators=[FileExtensionValidator(allowed_extensions=['mp3',])], blank=True)
    comment = models.TextField(blank=True)
    file_bool = models.FileField(upload_to='files/ordersresult', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])], blank=True)

    def __str__(self) -> str:
        return self.imam.username
