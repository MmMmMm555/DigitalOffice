from rest_framework import generics, parsers, serializers
from django.http import HttpResponse

from apps.common.permissions import IsSuperAdmin, IsImam, Role
from .serializers import (FridayThesisSerializer, FridayThesisCreateSerializer,
                          FridayThesisUpdateSerializer, FridayThesisDetailSerializer)
from apps.friday_tesis import models
from apps.friday_tesis.admin import FridayThesisResource


class FridayThesisCreateView(generics.CreateAPIView):
    queryset = models.FridayThesis.objects.all()
    serializer_class = FridayThesisCreateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser)


class FridayThesisUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.FridayThesis.objects.all()
    serializer_class = FridayThesisUpdateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser,)


class FridayThesisListView(generics.ListAPIView):
    queryset = models.FridayThesis.objects.only('id', 'title', 'types', 'to_region',
                                            'to_district', 'date', 'created_at',).prefetch_related('to_region', 'to_district',)
    serializer_class = FridayThesisSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    search_fields = ('title',)
    filterset_fields = ('id', 'date', 'created_at',
                        'to_region', 'to_district', 'types',)

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        query = self.queryset
        if start_date:
            query = query.filter(created_at__gte=start_date)
        if finish_date:
            query = query.filter(created_at__lte=finish_date)
        return query

    def get(self, request, *args, **kwargs):
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        excel = self.request.GET.get('excel')
        if excel == 'true':
            query = self.queryset
            if start_date:
                query = query.filter(created_at__gte=start_date)
            if finish_date:
                query = query.filter(created_at__lte=finish_date)
            for i in self.filterset_fields:
                filters = request.GET.get(i)
                filter = i
                if filters:
                    query = query.filter(**{filter: filters})
            data = FridayThesisResource().export(queryset=query)
            response = HttpResponse(data.xlsx, content_type='xlsx')
            response['Content-Disposition'] = "attachment; filename=thesis_data.xlsx"
            return response
        else:
            return self.list(request, *args, **kwargs)


class FridayThesisDetailView(generics.RetrieveDestroyAPIView):
    queryset = models.FridayThesis.objects.all().prefetch_related('to_region', 'to_district', 'to_mosque',)
    serializer_class = FridayThesisDetailSerializer
    permission_classes = (IsSuperAdmin | IsImam,)

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsSuperAdmin(),)
        return (IsImam() | IsSuperAdmin())

    # def perform_destroy(self, instance):
    #     if self.request.user.role == Role.SUPER_ADMIN:
    #         instance.delete()
    #     else:
    #         raise serializers.ValidationError(
    #             {'detail': 'you are not allowed to delete'})
