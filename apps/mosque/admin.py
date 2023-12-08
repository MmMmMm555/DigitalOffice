from django.contrib import admin

# Register your models here.
from apps.mosque.models import Mosque, FireDefenceImages, FireDefence

admin.site.register(Mosque)
admin.site.register(FireDefenceImages)