from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.models import DirectionsEmployeeRead, States, DirectionTypes, Directions, ToRole
from apps.common.regions import Regions


@api_view(['GET'])
def StatisticDirectionTypeApi(request):
    all = Directions.objects.all().count()
    data = {'count_all': all}
    for i in DirectionTypes:
        directions = Directions.objects.filter(direction_type=i).count()
        to_add = {'count': directions, "protsent": float(
            f"{(directions/all)*100:10.1f}")}
        data[i.value] = to_add
    return Response(data=data)


@api_view(['GET'])
def StatisticRegionApi(request):
    all = Directions.objects.all().count()
    data = {'count_all': all}
    for i in Regions.objects.all().values('id', 'name'):
        directions = Directions.objects.filter(to_region=i['id']).count()
        to_add = {'count': directions, "protsent": float(
            f"{(directions/all)*100:10.1f}")}
        data[i['name']] = to_add
    return Response(data=data)


@api_view(['GET'])
def StatisticRoleApi(request):
    all = Directions.objects.all().count()
    data = {'count_all': all}
    for i in ToRole:
        directions = Directions.objects.filter(to_role__contains=[i]).count()
        to_add = {'count': directions,}
        data[i.value] = to_add
    return Response(data=data)


@api_view(['GET'])
def StatisticStateApi(request):
    all = DirectionsEmployeeRead.objects.all().count()
    data = {'count_all': all}
    for i in States:
        directions = DirectionsEmployeeRead.objects.filter(state=i).count()
        to_add = {'count': directions, "protsent": float(
            f"{(directions/all)*100:10.1f}")}
        data[i.value] = to_add
    return Response(data=data)
