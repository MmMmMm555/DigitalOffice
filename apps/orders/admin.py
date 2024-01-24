from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget

from .models import Directions, Mosque
from apps.common.regions import Regions, Districts


class DirectionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Directions, DirectionsAdmin)


class DirectionsResource(ModelResource):
    to_region = Field(
        attribute='to_region',
        widget=ManyToManyWidget(Regions, field='name', separator=','),
    )
    to_district = Field(
        attribute='to_district',
        widget=ManyToManyWidget(Districts, field='name', separator=','),
    )
    to_mosque = Field(
        attribute='to_employee',
        widget=ManyToManyWidget(Mosque, field='name', separator=','),
    )

    required_to_region = Field(
        attribute='required_to_region',
        widget=ManyToManyWidget(Regions, field='name', separator=','),
    )
    required_to_district = Field(
        attribute='required_to_district',
        widget=ManyToManyWidget(Districts, field='name', separator=','),
    )
    required_to_mosque = Field(
        attribute='required_to_employee',
        widget=ManyToManyWidget(Mosque, field='name', separator=','),
    )

    class Meta:
        model = Directions
        fields = ('creator__username',
                  'title',
                  'direction_type',
                  'comments',
                  'types',
                  'from_role',
                  'to_role',
                  'to_region',
                  'to_district',
                  'to_mosque',
                  'required_to_region',
                  'required_to_district',
                  'required_to_mosque',
                  'from_date',
                  'to_date',
                  'image',
                  'video',
                  'comment',
                  'file_bool',)
        export_order = fields
