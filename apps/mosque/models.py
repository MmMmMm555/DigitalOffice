from django.db import models
from location_field.models.plain import PlainLocationField

from apps.common.models import BaseModel
from apps.common.regions import Districts

# Create your models here.


class MosqueTypeChoices(models.TextChoices):
    NEIGHBORHOOD = '1'
    JOME = '2'

class MosqueStatusChoices(models.TextChoices):
    GOOD = '1'
    REPAIR = '2'
    RECONSTRUCTION = '3'

class FireDefence(models.TextChoices):
    EVACUATION_ROAD = '1', 'evacuation_road'
    FIRE_SAFE = '2', 'fire_safe'
    FIRE_CLOSET = '3', 'fire_closet'
    FIRES_IGNAL = '4', 'fires_ignal'
    AUTO_FIRE_EXTINGUISHER = '5', 'auto_fire_extinguisher'

class FireDefenceImages(BaseModel):
    type = models.CharField(max_length=17, choices=FireDefence.choices, default=FireDefence.EVACUATION_ROAD)
    image = models.ImageField(upload_to='images/firedefence/')
    
    def __str__(self):
        return self.type


class Mosque(BaseModel):
    # other fields
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=355)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, related_name='mosque')
    location = PlainLocationField(based_fields=['city'], zoom=7)

    built_at = models.DateField()
    registered_at = models.DateField()
    
    parking = models.BooleanField(default=False)
    parking_capasity = models.IntegerField(blank=True, null=True)
    
    basement = models.BooleanField(default=False)
    second_floor = models.BooleanField(default=False)
    third_floor = models.BooleanField(default=False)
    cultural_heritage = models.BooleanField(default=False)
    fire_safety = models.BooleanField(default=False)
    auto_fire_extinguisher = models.BooleanField(default=False)
    fire_closet = models.BooleanField(default=False)
    fire_signal = models.BooleanField(default=False)
    
    service_rooms_bool = models.BooleanField(default=False)
    imam_room = models.BooleanField(default=False)
    sub_imam_room = models.BooleanField(default=False)
    casher_room = models.BooleanField(default=False)
    guard_room = models.BooleanField(default=False)
    other_room = models.BooleanField(default=False)
    other_room_amount = models.IntegerField(default=0, blank=True)
    
    fire_images = models.ManyToManyField(FireDefenceImages, blank=True)
    
    mosque_status = models.CharField(
        max_length=17, choices=MosqueStatusChoices.choices
    )
    mosque_type = models.CharField(
        max_length=17, choices=MosqueTypeChoices.choices
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Masjid'
        verbose_name_plural = 'Masjidlar'


# class FireSafe(BaseModel):
#     mosque = models.ForeignKey(
#         Mosque, on_delete=models.CASCADE, related_name='fire_safes')
#     image = models.ImageField(upload_to='image/firesafety/')

# class FireCloset(BaseModel):
#     mosque = models.ForeignKey(
#         Mosque, on_delete=models.CASCADE, related_name='firecloset')
#     image = models.ImageField(upload_to='image/firecloset/')

# class FireSignal(BaseModel):
#     mosque = models.ForeignKey(
#         Mosque, on_delete=models.CASCADE, related_name='firesignal')
#     image = models.ImageField(upload_to='image/firesignal/')

# class AutoFireExtinguisher(BaseModel):
#     mosque = models.ForeignKey(
#         Mosque, on_delete=models.CASCADE, related_name='autofireextinguisher')
#     image = models.ImageField(upload_to='image/autofireextinguisher/')

# class EvacuationRoad(BaseModel):
#     mosque = models.ForeignKey(
#         Mosque, on_delete=models.CASCADE, related_name='evacuation_roads'
#     )
#     image = models.ImageField(upload_to='images/evacuationroad/')