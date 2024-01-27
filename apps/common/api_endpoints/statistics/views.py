from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum, Q

from apps.orders.models import DirectionsEmployeeRead, States, DirectionTypes, Directions, ToRole
from apps.common.regions import Regions
from apps.friday_tesis.models import FridayThesisImamRead, FridayThesisImamResult
from apps.mosque.models import Mosque, MosqueTypeChoices, MosqueStatusChoices
from apps.employee.models import Employee, Graduation, Education, AcademicDegree

from rest_framework.views import APIView


# for orders

class StatisticDirectionTypeApi(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        finish_date = request.GET.get('finish_date')
        query = Directions.objects.all()

        if start_date and finish_date:
            query = query.filter(created_at__range=[start_date, finish_date])

        all_count = query.count()
        data = {'count_all': all_count}

        for i in DirectionTypes:
            directions = query.filter(direction_type=i).count()
            percentage = float(f"{(directions / all_count) * 100:10.1f}")
            to_add = {'count': directions, "percentage": percentage}
            data[i.value] = to_add

        return Response(data=data)


class StatisticRegionApi(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        finish_date = request.GET.get('finish_date')
        query = Directions.objects.all()

        if start_date and finish_date:
            query = query.filter(created_at__range=[start_date, finish_date])

        all_count = query.aggregate(all_count=Count('id'))['all_count']
        data = {'count_all': all_count}

        for region in Regions.objects.all().values('id', 'name'):
            directions = query.aggregate(
                count=Count('to_region', filter=Q(to_region__id=region['id']))
            )['count']

            percentage = float(f"{(directions / all_count) * 100:10.1f}")
            to_add = {'count': directions, "percentage": percentage}
            data[region['name']] = to_add

        return Response(data=data)


class StatisticRoleApi(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        finish_date = request.GET.get('finish_date')
        query = Directions.objects.all()

        if start_date and finish_date:
            query = query.filter(created_at__range=[start_date, finish_date])

        all_count = query.count()
        data = {'count_all': all_count}

        for role in ToRole:
            directions = query.filter(to_role__contains=[role]).count()
            to_add = {'count': directions}
            data[role.value] = to_add

        return Response(data=data)


class StatisticStateApi(APIView):
    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        finish_date = request.GET.get('finish_date')
        query = DirectionsEmployeeRead.objects.all()

        if start_date and finish_date:
            query = query.filter(created_at__range=[start_date, finish_date])

        all_count = query.count()
        data = {'count_all': all_count}

        state_counts = query.values('state').annotate(count=Count('state'))
        for state_count in state_counts:
            state = state_count['state']
            directions = state_count['count']
            percentage = float(f"{(directions / all_count) * 100:10.1f}")
            to_add = {'count': directions, 'percentage': percentage}
            data[state] = to_add

        return Response(data=data)


# for thesis
@api_view(['GET'])
def StatisticThesisStateApi(request):
    start_date = request.GET.get('start_date')
    finish_date = request.GET.get('finish_date')
    query = FridayThesisImamRead.objects.all()
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
    query = FridayThesisImamResult.objects.all()
    if start_date and finish_date:
        query = query.filter(created_at__range=[start_date, finish_date])
    all = query.aggregate(child=Sum(
        'child'), man=Sum('man'), old_man=Sum('old_man'), old=Sum('old'))
    all['count_all'] = sum(all.values())
    return Response(data=all)


# for mosques
@api_view(['GET'])
def StatisticMosqueTopApi(request):
    query = Mosque.objects.all().order_by(
        '-capacity').values('name', 'capacity')[:10]
    return Response(data=query)


@api_view(['GET'])
def StatisticMosqueTypeApi(request):
    query = Mosque.objects.all().aggregate(all_count=Count('id'), jame=Count('id', filter=Q(mosque_type=MosqueTypeChoices.JAME)),
                                           neighborhood=Count('id', filter=Q(mosque_type=MosqueTypeChoices.NEIGHBORHOOD)))
    return Response(data=query)


@api_view(['GET'])
def StatisticMosqueStatusApi(request):
    query = Mosque.objects.all().aggregate(all_count=Count('id'), good=Count('id', filter=Q(mosque_status=MosqueStatusChoices.GOOD)),
                                           repair=Count('id', filter=Q(mosque_status=MosqueStatusChoices.REPAIR)), reconstruction=Count('id', filter=Q(mosque_status=MosqueStatusChoices.RECONSTRUCTION)))
    return Response(data=query)


@api_view(['GET'])
def StatisticMosqueRegionApi(request):
    all = Mosque.objects.all()
    data = {'count_all': all.aggregate(all_count=Count('id'))['all_count']}
    for i in Regions.objects.all().values('id', 'name'):
        data[i['name']] = all.aggregate(region=Count(
            'id', filter=Q(region=i['id'])))['region']
    return Response(data=data)


# for employee
@api_view(['GET'])
def StatisticEmployeeUniversityApi(request):
    all = Employee.objects.all().exclude(graduated_univer=None)
    data = {'count_all': all.aggregate(all_count=Count('id'))['all_count']}
    for i in Graduation.objects.all().values('id', 'name'):
        data[i['name']] = all.aggregate(university=Count(
            'id', filter=Q(graduated_univer=i['id'])))['university']
    return Response(data=data)


@api_view(['GET'])
def StatisticEmployeeEducationApi(request):
    all = Employee.objects.all().aggregate(
        all_count=Count('id'), 
        medium_special=Count('id', filter=Q(education=Education.MEDIUM_SPECIAL)), 
        high=Count('id', filter=Q(education=Education.HIGH)), 
        none=Count('id', filter=Q(education=Education.NONE)),)
    return Response(data=all)


@api_view(['GET'])
def StatisticEmployeeAcademicDegreeApi(request):
    all = Employee.objects.all().aggregate(
        all_count=Count('id'), 
        bachelor=Count('id', filter=Q(education=AcademicDegree.BACHELOR)), 
        master=Count('id', filter=Q(education=AcademicDegree.MASTER)), 
        phd=Count('id', filter=Q(education=AcademicDegree.PhD)), 
        dsc=Count('id', filter=Q(education=AcademicDegree.DsC)),
        none=Count('id', filter=Q(education=AcademicDegree.NONE)))
    return Response(data=all)