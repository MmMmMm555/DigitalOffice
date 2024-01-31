from core.celery import app
from datetime import date, timedelta
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from django.db import transaction

from . import models
from apps.users.models import Role, User


@app.task
def create_thesis_notifications(thesis):
    with transaction.atomic():
        thesis = models.FridayThesis.objects.get(id=thesis)
        imams = User.objects.filter(role=Role.IMAM)
        notifications_to_create = [models.FridayThesisImamResult(
            tesis=thesis,
            imam=i,
        ) for i in imams]
        models.FridayThesisImamResult.objects.bulk_create(
            notifications_to_create)
        seen = models.FridayThesisImamResult.objects.filter(tesis=thesis)

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
    return True


@app.task
def check_delayed_results():
    today = date.today() - timedelta(days=1)
    try:
        thesis = get_object_or_404(models.FridayThesis, date=today)
        notifications = models.FridayThesisImamResult.objects.filter(
            tesis=thesis, state=models.States.UNSEEN)
        notifications.update(state=models.States.DELAYED)
        return True
    except Http404:
        return False
