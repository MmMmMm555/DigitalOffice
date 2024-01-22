from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from .models import User


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(User, UserAdmin)


class UserResource(ModelResource):
    class Meta:
        model = User
        fields = ('username', 'region__name',
                  'district__name', 'role', 'email',)
        export_order = fields
