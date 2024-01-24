from django.contrib import admin
from django.apps import apps
from apps.employee.models import Employee
from apps.friday_tesis.models import FridayThesis


models = apps.get_models()

for model in models:
    try:
        if model != Employee and model != FridayThesis:
            admin.site.register(model)
    except:
        pass
