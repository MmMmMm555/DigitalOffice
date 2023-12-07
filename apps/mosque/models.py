from django.db import models
from location_field.models.plain import PlainLocationField

from apps.common.models import BaseModel
# from apps.attribute.models import Attribute, AttributeOption

# Create your models here.


class MosqueTypeChoices(models.Choices):
    SIMPLE = 'oddiy'
    JOME = 'jome'


class MosqueStatusChoices(models.Choices):
    GOOD = 'Yaxshi'
    REPAIR = 'Tamir talab'
    RECONSTRUCTION = 'Qayta qurish'


class Heritage(BaseModel):
    title = models.CharField(max_length=255)


class AutoFireClear(BaseModel):
    image = models.ImageField(upload_to='autofireclear/')


class FireCloset(BaseModel):
    image = models.ImageField(upload_to='firecloset/')


class FireSignal(BaseModel):
    image = models.ImageField(upload_to='fire_signal/')


class Mosque(BaseModel):
    # other fields
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    location = PlainLocationField(based_fields=['city'], zoom=7)

    built_at = models.DateField()
    registered_at = models.DateField()
    parking_capasity = models.IntegerField(blank=True, null=True)

    mosque_status = models.CharField(
        max_length=255, choices=MosqueStatusChoices.choices
    )
    mosque_type = models.CharField(
        max_length=255, choices=MosqueTypeChoices.choices
    )

    heritage = models.ForeignKey(Heritage, on_delete=models.CASCADE)
    auto_fire_clear = models.ForeignKey(AutoFireClear, on_delete=models.CASCADE)  # noqa
    fire_closet = models.ForeignKey(FireCloset, on_delete=models.CASCADE)
    fire_signal = models.ForeignKey(FireSignal, on_delete=models.CASCADE)


class Room(BaseModel):
    mosque = models.ForeignKey(
        Mosque, on_delete=models.CASCADE, related_name='rooms')
    title = models.CharField(max_length=255)
    room_count = models.IntegerField(blank=True, null=True)


class FireSafe(BaseModel):
    mosque = models.ForeignKey(
        Mosque, on_delete=models.CASCADE, related_name='fire_safes')
    image = models.ImageField(upload_to='iimage/firesafety/')


class EvacuationRoad(BaseModel):
    mosque = models.ForeignKey(
        Mosque, on_delete=models.CASCADE, related_name='evacuation_roads'
    )
    image = models.ImageField(upload_to='images/evacuationroad/')


# class MosqueAttributeValue(BaseModel):
#     mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name='attribute_values')
#     attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
#     value = models.CharField(max_length=255)

# class MosqueAttributeOptionValue(BaseModel):
#     mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name='attribute_value_options')
#     attribute = models.ForeignKey(AttributeOption, on_delete=models.CASCADE)
