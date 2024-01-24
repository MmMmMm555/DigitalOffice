from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget

from .models import FridayThesis, Mosque
from apps.common.regions import Regions, Districts


class FridayThesisAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(FridayThesis, FridayThesisAdmin)


class FridayThesisResource(ModelResource):
    to_region = Field(
        attribute='to_region',
        widget=ManyToManyWidget(Regions, field='name', separator=','),
    )
    to_district = Field(
        attribute='to_district',
        widget=ManyToManyWidget(Districts, field='name', separator=','),
    )

    to_mosque = Field(
        attribute='to_mosque',
        widget=ManyToManyWidget(Mosque, field='name', separator=','),
    )

    class Meta:
        model = FridayThesis
        fields = ("title",
                  "types",
                  "file_comment",
                  "attachment_comment",
                  "date",
                  "to_region",
                  "to_district",
                  "to_mosque",
                  "image",
                  "video",
                  "comment",
                  "file_bool",)
        export_order = fields
