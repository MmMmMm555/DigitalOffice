from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from .models import Mosque


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Mosque, UserAdmin)


class MosqueResource(ModelResource):
    class Meta:
        model = Mosque
        fields = (
            'name',
            'address',
            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'region__name',
            'district__name',
            'built_at',
            'registered_at',
            'parking',
            'basement',
            'capacity',
            'second_floor',
            'third_floor',
            'cultural_heritage',
            'graveyard',)
        export_order = fields
