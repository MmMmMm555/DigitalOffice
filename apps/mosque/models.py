from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from location_field.models.plain import PlainLocationField

from apps.common.models import BaseModel
from apps.common.regions import Districts

# Create your models here.


class MosqueTypeChoices(models.TextChoices):
    NEIGHBORHOOD = '1'
    JOME = '2'

class MosqueHeatingTypeChoices(models.TextChoices):
    CENTRAL = '1'
    LOCAL = '2'

class MosqueHeatingFuelChoices(models.TextChoices):
    GAS = '1'
    LIQUID_FUEL = '2'
    SOLID_FUEL = '3'
    NONE = '4'

class MosqueStatusChoices(models.TextChoices):
    GOOD = '1'
    REPAIR = '2'
    RECONSTRUCTION = '3'

class FireDefense(models.TextChoices):
    EVACUATION_ROAD = '1'
    FIRE_SAFE = '2'
    FIRE_CLOSET = '3'
    FIRE_SIGNAL = '4'
    AUTO_FIRE_EXTINGUISHER = '5'

class FireDefenseImages(BaseModel):
    type = models.CharField(max_length=17, choices=FireDefense.choices, default=FireDefense.EVACUATION_ROAD)
    image = models.ImageField(upload_to='images/firedefence/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")
    
    def __str__(self):
        return str(self.id)


class Mosque(BaseModel):
    # other fields
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=355)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, related_name='mosque')
    location = PlainLocationField(based_fields=['city'], zoom=10)

    built_at = models.DateField()
    registered_at = models.DateField()

    parking = models.BooleanField(default=False)
    parking_capacity = models.IntegerField(default=0, blank=True)

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
    
#capacity = models.PositiveIntegerField(default=0, blank=False) 
    
    mosque_library = models.BooleanField(default=False)

    fire_images = models.ManyToManyField(FireDefenseImages, blank=True)
    
    mosque_status = models.CharField(
        max_length=17, choices=MosqueStatusChoices.choices,
        default=MosqueStatusChoices.GOOD,
    )
    mosque_type = models.CharField(
        max_length=17, choices=MosqueTypeChoices.choices,
        default=MosqueTypeChoices.JOME,
    )
    mosque_heating_type = models.CharField(
        max_length=17, choices=MosqueHeatingTypeChoices.choices,
        default=MosqueHeatingTypeChoices.CENTRAL,
    )
    mosque_heating_fuel = models.CharField(
        max_length=17, choices=MosqueHeatingFuelChoices.choices,
        default=MosqueHeatingFuelChoices.NONE,
    )
    
    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        ordering = ['-created_at',]
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