from django.contrib import admin
from django.apps import apps
from apps.employee.models import Employee
# Register your models here.

models = apps.get_models()

for model in models:
    try:
        if model != Employee:
            admin.site.register(model)
    except:
        pass
