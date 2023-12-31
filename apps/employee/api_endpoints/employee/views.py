from rest_framework import generics, parsers, permissions, filters, viewsets
from apps.common.permissions import IsSuperAdmin
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date

from . import serializers
from apps.employee import models


class EmployeeListView(generics.ListAPIView):
    """ hodimlarni yosh boyicha filter qilish uchun "start_age" va "finish_age" filterlariga qiymat yuboriladi, "start_age < finish_age" ! """
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeListSerializer
    permission_classes = (IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('name', 'surname', 'last_name',)
    filterset_fields = ('id', 'birth_date', 'education',
                        'graduated_year', 'academic_degree', 'profile__role',)

    def get_queryset(self):
        start_age = self.request.GET.get('start_age')
        finish_age = self.request.GET.get('finish_age')
        query = self.queryset
        if start_age and finish_age and start_age < finish_age:
            current_year = date.today().year
            print(current_year)
            start_year = current_year-int(finish_age)
            finish_year = current_year-int(start_age)
            query = query.filter(birth_date__year__range=[start_year, finish_year])
        return query

class EmployeeCreateView(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser)
    permission_classes = (IsSuperAdmin,)


class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeUpdateSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)
    permission_classes = (IsSuperAdmin,)


class EmployeeDetailView(generics.RetrieveDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = (IsSuperAdmin,)


class SocialMediaView(viewsets.ModelViewSet):
    queryset = models.SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer
    pagination_class = None
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'employee', 'social_media',)
    lookup_field = 'pk'
