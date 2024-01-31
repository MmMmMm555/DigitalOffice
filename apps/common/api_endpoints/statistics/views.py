from rest_framework.response import Response
from django.db.models import Count, Sum, Q
from rest_framework import status
from rest_framework.views import APIView

from apps.orders.models import DirectionsEmployeeRead, States, DirectionTypes, Directions, ToRole
from apps.common.regions import Regions
from apps.friday_tesis.models import FridayThesisImamRead, FridayThesisImamResult
from apps.mosque.models import Mosque, MosqueTypeChoices, MosqueStatusChoices
from apps.employee.models import Employee, Graduation, Education, AcademicDegree


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

        if start_date:
            query = query.filter(created_at__gte=start_date)
        if finish_date:
            query = query.filter(created_at__lte=finish_date)

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

class StatisticThesisStateApi(APIView):
    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        finish_date = self.request.query_params.get('finish_date')

        query = FridayThesisImamRead.objects.all()
        if start_date:
            query = query.filter(created_at__gte=start_date)
        if finish_date:
            query = query.filter(created_at__lte=finish_date)

        all_stats = query.aggregate(
            unseen=Count('state', filter=Q(state=States.UNSEEN)),
            accepted=Count('state', filter=Q(state=States.ACCEPTED)),
            done=Count('state', filter=Q(state=States.DONE)),
        )

        total_count = sum(all_stats.values())
        if total_count > 0:
            for state, count in all_stats.items():
                percentage = (count / total_count) * 100
                all_stats[state] = {'count': count,
                                    'percentage': float(f"{percentage:10.1f}")}

            all_stats['count_all'] = total_count
        else:
            all_stats['count_all'] = 0

        return Response(data=all_stats, status=status.HTTP_200_OK)


class StatisticThesisAgeApi(APIView):
    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        finish_date = self.request.query_params.get('finish_date')

        query = FridayThesisImamResult.objects.all()
        if start_date:
            query = query.filter(created_at__gte=start_date)
        if finish_date:
            query = query.filter(created_at__lte=finish_date)

        all_stats = query.aggregate(
            child=Sum('child'),
            man=Sum('man'),
            old_man=Sum('old_man'),
            old=Sum('old'),
        )

        total_count = sum(all_stats.values())
        if total_count > 0:
            for age_group, count in all_stats.items():
                percentage = (count / total_count) * 100
                all_stats[age_group] = {'count': count,
                                        'percentage': float(f"{percentage:10.1f}")}

            all_stats['count_all'] = total_count
        else:
            all_stats['count_all'] = 0

        return Response(data=all_stats, status=status.HTTP_200_OK)


# for mosques

class StatisticMosqueTopApi(APIView):
    def get(self, request, *args, **kwargs):
        mosques = Mosque.objects.all().order_by(
            '-capacity').values('name', 'capacity')[:10]
        return Response(data=mosques, status=status.HTTP_200_OK)


class StatisticMosqueTypeApi(APIView):
    def get(self, request, *args, **kwargs):
        query = Mosque.objects.all().aggregate(
            all_count=Count('mosque_type'),
            jame=Count('mosque_type', filter=Q(
                mosque_type=MosqueTypeChoices.JAME)),
            neighborhood=Count('mosque_type', filter=Q(
                mosque_type=MosqueTypeChoices.NEIGHBORHOOD))
        )

        total_count = query['all_count']

        if total_count > 0:
            for mosque_type, count in query.items():
                if mosque_type != 'all_count':
                    percentage = (count / total_count) * 100
                    query[mosque_type] = {'count': count,
                                          'percentage': float(f"{percentage:10.1f}")}

        else:
            query['all_count'] = 0

        return Response(data=query, status=status.HTTP_200_OK)


class StatisticMosqueStatusApi(APIView):
    def get(self, request, *args, **kwargs):
        query = Mosque.objects.all().aggregate(
            all_count=Count('id'),
            good=Count('id', filter=Q(mosque_status=MosqueStatusChoices.GOOD)),
            repair=Count('id', filter=Q(
                mosque_status=MosqueStatusChoices.REPAIR)),
            reconstruction=Count('id', filter=Q(
                mosque_status=MosqueStatusChoices.RECONSTRUCTION))
        )

        total_count = query['all_count']

        if total_count > 0:
            for status, count in query.items():
                if status != 'all_count':
                    percentage = (count / total_count) * 100
                    query[status] = {'count': count,
                                     'percentage': float(f"{percentage:10.1f}")}
        else:
            query['all_count'] = 0

        return Response(data=query)


class StatisticMosqueRegionApi(APIView):
    def get(self, request, *args, **kwargs):
        all = Mosque.objects.all()
        data = {'count_all': all.aggregate(all_count=Count('id'))['all_count']}

        for region in Regions.objects.all().values('id', 'name'):
            region_count = all.aggregate(region=Count(
                'id', filter=Q(region=region['id'])))['region']
            data[region['name']] = {'count': region_count}

            total_count = data['count_all']
            if total_count > 0:
                percentage = (region_count / total_count) * 100
                data[region['name']]['percentage'] = float(
                    f"{percentage:10.1f}")
            else:
                data[region['name']]['percentage'] = 0.0

        return Response(data=data, status=status.HTTP_200_OK)


# for employee

class StatisticEmployeeUniversityApi(APIView):
    def get(self, request, *args, **kwargs):
        all_employees = Employee.objects.all().exclude(graduated_univer=None)
        data = {'count_all': all_employees.aggregate(
            all_count=Count('id'))['all_count']}

        for graduation in Graduation.objects.all().values('id', 'name'):
            graduation_count = all_employees.aggregate(university=Count(
                'id', filter=Q(graduated_univer=graduation['id'])))['university']
            data[graduation['name']] = {'count': graduation_count}

            total_count = data['count_all']
            if total_count > 0:
                percentage = (graduation_count / total_count) * 100
                data[graduation['name']]['percentage'] = float(
                    f"{percentage:10.1f}")
            else:
                data[graduation['name']]['percentage'] = 0.0

        return Response(data=data, status=status.HTTP_200_OK)


class StatisticEmployeeEducationApi(APIView):
    def get(self, request, *args, **kwargs):
        total_count = Employee.objects.count()

        education_data = Employee.objects.values('education').annotate(
            count=Count('id'),
            percentage=Count('id') * 100 /
            total_count if total_count > 0 else 0
        )

        data = {
            education['education']: {
                'count': education['count'],
                'percentage': float(f"{education['percentage']:10.1f}"),
            }
            for education in education_data
        }

        data['all_count'] = total_count

        return Response(data=data, status=status.HTTP_200_OK)


class StatisticEmployeeAcademicDegreeApi(APIView):
    def get(self, request, *args, **kwargs):
        total_count = Employee.objects.count()

        degree_data = Employee.objects.values('education').annotate(
            count=Count('id'),
            percentage=Count('id') * 100 /
            total_count if total_count > 0 else 0
        )

        data = {
            degree['education']: {
                'count': degree['count'],
                'percentage': float(f"{degree['percentage']:10.1f}"),
            }
            for degree in degree_data
        }

        data['all_count'] = total_count

        return Response(data=data, status=status.HTTP_200_OK)
