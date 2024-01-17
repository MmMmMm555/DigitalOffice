from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

# Register your models here.


class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(Employee, EmployeeAdmin)

class EmployeeResource(ModelResource):
    class Meta:
        model = Employee
        fields = ('name', 'surname', 'last_name', 'birth_date', 'phone_number', 'address', 'gender', 'nation', 'diploma_number', 'mosque__name', 'graduated_univer__name', 'graduated_year',)
        export_order = ('name', 'surname', 'last_name', 'birth_date', 'phone_number', 'address', 'gender', 'nation', 'diploma_number', 'mosque__name', 'graduated_univer__name', 'graduated_year',)