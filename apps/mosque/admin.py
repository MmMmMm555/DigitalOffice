from django.contrib import admin

# Register your models here.
from apps.mosque.models import Mosque, MosqueAttributeOptionValue, MosqueAttributeValue


class MosqueAttributeValueStackedInline(admin.StackedInline):
    model = MosqueAttributeValue
    extra = 1


class MosqueAttributeOptionValueStackedInline(admin.StackedInline):
    model = MosqueAttributeOptionValue
    extra = 1


@admin.register(Mosque)
class MosqueAdmin(admin.ModelAdmin):
    # fields = [
    #     'title',
    #     'address',
    #     'location',
    # ]
    inlines = [
        MosqueAttributeValueStackedInline,
        MosqueAttributeOptionValueStackedInline
    ]
    list_display = [
        'title',
        'address',
        'location',
        'built_at',
        'registered_at',
        'mosque_type',
        'mosque_status'
    ]
