from django.db import models

from apps.common.models import BaseModel

# Create your models here.


class AttributeTypeChoices(models.Choices):
    BUTTON = 'button'
    TEXT = 'text'
    SELECT = 'select'
    MULTISELECT = 'multiselect'


class AttributeFilterType(models.TextChoices):
    RANGE = "range"
    MULTISELECT = "multiselect"


class Attribute(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="category_attributes/", null=True, blank=True)
    type = models.CharField(
        max_length=255, choices=AttributeTypeChoices.choices, default=AttributeTypeChoices.TEXT
    )
    # filter_type = models.CharField(
    #     max_length=255,
    #     choices=AttributeFilterType.choices,
    #     default=AttributeFilterType.RANGE,
    # )

    is_required = models.BooleanField(default=False)
    is_list = models.BooleanField(default=False)
    is_filter = models.BooleanField(default=False)

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ("order",)


class AttributeOption(BaseModel):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="options"
    )

    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ("order",)
