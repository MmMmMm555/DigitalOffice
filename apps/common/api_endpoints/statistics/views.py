from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum, Q

from apps.orders.models import DirectionsEmployeeRead, States, DirectionTypes, Directions, ToRole
from apps.common.regions import Regions
from apps.friday_tesis.models import FridayTesisImamRead, FridayTesisImamResult


# for orders
@api_view(['GET'])
def StatisticDirectionTypeApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = Directions.objects.all()
    if start_date and finish_date:
        query = query.filter(created_at__range=[start_date, finish_date])
    all = query.count()
    data = {'count_all': all}
    for i in DirectionTypes:
        directions = query.filter(direction_type=i).count()
        to_add = {'count': directions, "protsent": float(
            f"{(directions/all)*100:10.1f}")}
        data[i.value] = to_add
    return Response(data=data)


@api_view(['GET'])
def StatisticRegionApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = Directions.objects.all()
    if start_date and finish_date:
        query = query.filter(created_at__range=[start_date, finish_date])
    all = query.count()
    data = {'count_all': all}
    for i in Regions.objects.all().values('id', 'name'):
        directions = query.filter(to_region=i['id']).count()
        to_add = {'count': directions, "protsent": float(
            f"{(directions/all)*100:10.1f}")}
        data[i['name']] = to_add
    return Response(data=data)


@api_view(['GET'])
def StatisticRoleApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = Directions.objects.all()
    if start_date and finish_date:
        query = query.filter(created_at__range=[start_date, finish_date])
    all = query.count()
    data = {'count_all': all}
    for i in ToRole:
        directions = query.filter(to_role__contains=[i]).count()
        to_add = {'count': directions, }
        data[i.value] = to_add
    return Response(data=data)


@api_view(['GET'])
def StatisticStateApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = DirectionsEmployeeRead.objects.all()
    if start_date and finish_date:
        query = query.filter(created_at__range=[start_date, finish_date])
    all = query.count()
    data = {'count_all': all}
    for i in States:
        directions = query.filter(state=i).count()
        to_add = {'count': directions, "protsent": float(
            f"{(directions/all)*100:10.1f}")}
        data[i.value] = to_add
    return Response(data=data)


# for thesis
@api_view(['GET'])
def StatisticThesisStateApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = FridayTesisImamRead.objects.all()
    if start_date and finish_date:
        query = query.filter(created_at__range=[start_date, finish_date])
    all = query.aggregate(
        unseen=Count('state', filter=Q(state=States.UNSEEN)), accepted=Count('state', filter=Q(state=States.ACCEPTED)), done=Count('state', filter=Q(state=States.DONE)),)
    all['count_all'] = sum(all.values())
    return Response(data=all)


@api_view(['GET'])
def StatisticThesisAgeApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = FridayTesisImamResult.objects.all()
    if start_date and finish_date:
            query = query.filter(created_at__range=[start_date, finish_date])
    all = query.aggregate(child=Sum(
        'child'), man=Sum('man'), old_man=Sum('old_man'), old=Sum('old'))
    all['count_all'] = sum(all.values())
    return Response(data=all)
