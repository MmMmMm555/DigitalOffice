from rest_framework.generics import (CreateAPIView, ListAPIView,
                        UpdateAPIView, RetrieveAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (ArticleSerializer, ArticleListSerializer,
                          ArticleUpdateSerializer, ArticleDetailSerializer,)
from apps.scientific_activity.models import Article
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin
from rest_framework.response import Response
from apps.common.view_mixin import FilerQueryByRole


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class ArticleListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'type', 'date', 'created_at',)


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = (IsAuthenticated,)


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsSuperAdmin | IsImam | IsDeputy,)

    def delete(self, request, *args, **kwargs):
        if request.user == self.get_object().imam:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        return Response(status=403)


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer
    permission_classes = (IsSuperAdmin | IsImam | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)
