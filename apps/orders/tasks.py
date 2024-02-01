from core.celery import app
from datetime import date
from django.db import transaction

from . import models
from apps.users.models import User
from apps.common.regions import Districts


@app.task
def create_direction_notifications(direction_id):
    with transaction.atomic():
        # getting instance
        direction = models.Directions.objects.get(id=direction_id)
        # getting instance role
        to_role = direction.to_role
        # getting m2m field values
        employee = User.objects.filter(role__in=to_role)
        employee_list = direction.to_employee.all()
        district_list = direction.to_district.all()
        region_list = direction.to_region.all()
        # filtering m2m fields
        if not region_list:
            models.DirectionsEmployeeResult.objects.bulk_create(
                [
                    models.DirectionsEmployeeResult(
                        direction=direction, employee=i)
                    for i in employee
                ]
            )
        else:
            if region_list:
                employee = employee.filter(region__in=region_list)
            if district_list:
                employee = employee.filter(district__in=district_list)
            if employee_list:
                employee = employee.filter(
                    profil__mosque__id__in=employee_list)
            employee_to_create = [
                models.DirectionsEmployeeResult(
                    direction=direction, employee=i)
                for i in employee
            ]
            models.DirectionsEmployeeResult.objects.bulk_create(
                employee_to_create)

        # getting m2m require field values
        employee_required = employee
        employee_list_required = direction.required_to_employee.all()
        district_list_required = direction.required_to_district.all()
        region_list_required = direction.required_to_region.all()

        # filtering m2m required fields
        if employee_list_required:
            models.DirectionsEmployeeResult.objects.filter(
                direction=direction,
                employee__in=employee_required.filter(
                    profil__mosque__id__in=employee_list_required)
            ).update(requirement=True)
        elif district_list_required:
            employee_required = employee_required.filter(
                region__in=region_list_required, district__in=district_list_required)
            models.DirectionsEmployeeResult.objects.filter(
                direction=direction,
                employee__in=employee_required
            ).update(requirement=True)
        else:
            district_list_required = Districts.objects.filter(
                region__in=region_list_required)
            models.DirectionsEmployeeResult.objects.filter(
                direction=direction,
                employee__in=employee_required.filter(
                    district__in=district_list_required)
            ).update(requirement=True)
        return True


@app.task
def check_delayed_direction_results():
    today = date.today()
    direction = models.Directions.objects.filter(to_date=today)
    if direction:
        notifications = models.DirectionsEmployeeResult.objects.filter(
            direction__in=direction, state=models.States.UNSEEN)
        notifications.update(state=models.States.DELAYED)
        return True
    return False
