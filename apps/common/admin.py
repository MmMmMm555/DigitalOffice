from django.contrib import admin
from django.apps import apps
from apps.employee.models import Employee
from apps.friday_tesis.models import FridayThesis
from apps.orders.models import Directions


models = apps.get_models()

for model in models:
    try:
        if model not in [Employee, FridayThesis, Directions]:
            admin.site.register(model)
    except:
        pass
