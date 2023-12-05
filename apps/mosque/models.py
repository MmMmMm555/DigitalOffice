from django.db import models
from location_field.models.plain import PlainLocationField

from apps.common.models import BaseModel
from apps.attribute.models import Attribute, AttributeOption
# Create your models here.


class MosqueTypeChoices(models.Choices):
    SIMPLE = 'oddiy'
    JOME = 'jome'


class MosqueStatusChoices(models.Choices):
    GOOD = 'yaxshi'
    REPAIR = 'Tamir talab'
    RECONSTRUCTION = 'Qayta qurish'


class Mosque(BaseModel):
    # other fields
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    location = PlainLocationField(based_fields=['city'], zoom=7)

    built_at = models.DateField()
    registered_at = models.DateField()
    # parking_capasity = models.IntegerField(blank=True, null=True)


    mosque_status = models.CharField(
        max_length=255, choices=MosqueStatusChoices.choices
    )
    mosque_type = models.CharField(
        max_length=255, choices=MosqueTypeChoices.choices
    )


class MosqueAttributeValue(BaseModel):
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name='attribute_values')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

class MosqueAttributeOptionValue(BaseModel):
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name='attribute_value_options')
    attribute = models.ForeignKey(AttributeOption, on_delete=models.CASCADE)