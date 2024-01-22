from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from location_field.models.plain import PlainLocationField
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.common.regions import Districts, Regions
from apps.common.validators import validate_image_size


class MosqueTypeChoices(models.TextChoices):
    NEIGHBORHOOD = 'neighborhood'
    JAME = 'jame'


class MosqueHeatingTypeChoices(models.TextChoices):
    CENTRAL = 'central'
    LOCAL = 'local'


class MosqueHeatingFuelChoices(models.TextChoices):
    GAS = 'gas'
    LIQUID_FUEL = 'liquid_fuel'
    SOLID_FUEL = 'solid_fuel'
    NONE = 'none'


class MosqueStatusChoices(models.TextChoices):
    GOOD = 'good'
    REPAIR = 'repair'
    RECONSTRUCTION = 'reconstruction'


class FireDefense(models.TextChoices):
    EVACUATION_ROAD = 'evacuation_road'
    FIRE_SAFE = 'fire_safe'
    FIRE_CLOSET = 'fire_closet'
    FIRE_SIGNAL = 'fire_signal'
    AUTO_FIRE_EXTINGUISHER = 'auto_fire_extinguisher'
    EMERGENCY_EXIT_DOOR = 'emergency_exit_door'


class FireDefenseImages(BaseModel):
    type = models.CharField(verbose_name=_("type"),
        max_length=22, choices=FireDefense.choices, default=FireDefense.EVACUATION_ROAD)
    image = models.ImageField(verbose_name=_("image"), upload_to='images/fire_defense/', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Masjid rasmi '
        verbose_name_plural = 'Masjid rasmlari '

class Mosque(BaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    address = models.CharField(verbose_name=_("address"), max_length=355)
    region = models.ForeignKey(
        Regions, verbose_name=_("region"), on_delete=models.CASCADE, related_name='mosque_region')
    district = models.ForeignKey(
        Districts, verbose_name=_("district"), on_delete=models.CASCADE, related_name='mosque_district')
    location = PlainLocationField(verbose_name=_("location"), based_fields=['city'], zoom=10)
    image = models.ImageField(verbose_name=_("image"), upload_to='images/mosque/', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size],
                              help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True, default="images/default/default_mosque.png")

    built_at = models.DateField(verbose_name=_("built_at"), )
    registered_at = models.DateField(verbose_name=_("registered_at"), )

    parking = models.BooleanField(verbose_name=_("parking"), default=False)
    parking_capacity = models.IntegerField(verbose_name=_("parking_capacity"), default=0, blank=True)

    basement = models.BooleanField(verbose_name=_("basement"), default=False)
    second_floor = models.BooleanField(verbose_name=_("second_floor"), default=False)
    third_floor = models.BooleanField(verbose_name=_("third_floor"), default=False)

    cultural_heritage = models.BooleanField(verbose_name=_("cultural_heritage"), default=False)

    fire_safety = models.BooleanField(verbose_name=_("fire_safety"), default=False)
    auto_fire_extinguisher = models.BooleanField(verbose_name=_("auto_fire_extinguisher"), default=False)
    fire_closet = models.BooleanField(verbose_name=_("fire_closet"), default=False)
    fire_signal = models.BooleanField(verbose_name=_("fire_signal"), default=False)
    evacuation_road = models.BooleanField(verbose_name=_("evacuation_road"), default=False)
    emergency_exit_door = models.BooleanField(verbose_name=_("emergency_exit_door"), default=False)

    service_rooms_bool = models.BooleanField(verbose_name=_("service_rooms_bool"), default=False)
    imam_room = models.BooleanField(verbose_name=_("imam_room"), default=False)
    sub_imam_room = models.BooleanField(verbose_name=_("sub_imam_room"), default=False)
    casher_room = models.BooleanField(verbose_name=_("casher_room"), default=False)
    guard_room = models.BooleanField(verbose_name=_("guard_room"), default=False)
    other_room = models.BooleanField(verbose_name=_("other_room"), default=False)
    other_room_amount = models.IntegerField(verbose_name=_("other_room_amount"), default=0, blank=True)

    capacity = models.PositiveIntegerField(verbose_name=_("capacity"), default=0, blank=False)

    mosque_library = models.BooleanField(verbose_name=_("mosque_library"), default=False)
    shop = models.BooleanField(verbose_name=_("shop"), default=False)
    shrine = models.BooleanField(verbose_name=_("shrine"), default=False)
    graveyard = models.BooleanField(verbose_name=_("graveyard"), default=False)

    fire_images = models.ManyToManyField(FireDefenseImages, verbose_name=_("fire_images"), blank=True)

    mosque_status = models.CharField(verbose_name=_("mosque_status"), 
        max_length=17, choices=MosqueStatusChoices.choices,
        default=MosqueStatusChoices.GOOD,
    )
    mosque_type = models.CharField(verbose_name=_("mosque_type"), 
        max_length=17, choices=MosqueTypeChoices.choices,
        default=MosqueTypeChoices.JAME,
    )
    mosque_heating_type = models.CharField(verbose_name=_("mosque_heating_type"), 
        max_length=17, choices=MosqueHeatingTypeChoices.choices,
        blank=True,
    )
    mosque_heating_fuel = models.CharField(verbose_name=_("mosque_heating_fuel"), 
        max_length=17, choices=MosqueHeatingFuelChoices.choices,
        blank=True,
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Masjid'
        verbose_name_plural = 'Masjidlar'
