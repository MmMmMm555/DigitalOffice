from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from .models import User

admin.site.unregister(Group)


class UserResource(ModelResource):
    class Meta:
        model = User
        fields = ('username', 'region__name',
                  'district__name', 'role', 'email', 'profil__first_name', 'profil_last_name',)
        export_order = fields


class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (
        ("Login details", {'fields': ('username', 'password', )}),
        (_('User info'), {
         'fields': ('email', 'role', 'region', 'district', 'profil',)}),
        (_('Permissions'), {
         'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_filter = ("is_staff", "is_superuser", "is_active",
                   'role', 'region', 'district',)
    filter_horizontal = ()
    list_display = ('id', 'username',)
    list_display_links = ('id', 'username',)
    search_fields = ('username',)
    ordering = ('id', )


admin.site.register(User, UserAdmin)
