from celery import shared_task
from core.celery import app
from . import models
from apps.users.models import Role, User


@app.task
def create_thesis_notifications(thesis):
    thesis = models.FridayThesis.objects.get(id=thesis)
    imams = User.objects.filter(role=Role.IMAM)
    notifications_to_create = [models.FridayThesisImamRead(
        tesis=thesis,
        imam=i,
    ) for i in imams]
    models.FridayThesisImamRead.objects.bulk_create(
        notifications_to_create)
    seen = models.FridayThesisImamRead.objects.filter(tesis=thesis)

    mosque_list = thesis.to_mosque.all()
    district_list = thesis.to_district.all()
    region_list = thesis.to_region.all()

    if region_list:
        seen.filter(imam__in=imams.filter(
            region__in=region_list)).update(requirement=True)
    if district_list:
        seen.filter(imam__in=imams.filter(
            district__in=district_list)).update(requirement=True)
    if mosque_list:
        seen.filter(imam__in=imams.filter(
            profil__mosque__in=mosque_list)).update(requirement=True)

    # return "tesis"
