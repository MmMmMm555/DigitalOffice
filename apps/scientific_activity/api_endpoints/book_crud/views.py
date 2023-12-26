from rest_framework.generics import (CreateAPIView, ListAPIView,
                        RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (BookSerializer, BookListSerializer,
                          BookUpdateSerializer, BookDetailSerializer,)
from apps.scientific_activity.models import Book
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin
from rest_framework.response import Response


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'direction', 'date', 'created_at',)

    def get_queryset(self):
        if self.request.user.role in ['4', '5']:
            return Book.objects.filter(imam=self.request.user)
        elif self.request.user.role in ['1']:
            return Book.objects.all()
        elif self.request.user.role in ['2']:
            return Book.objects.filter(imam__region=self.request.user.region)
        elif self.request.user.role in ['3']:
            return Book.objects.filter(imam__district=self.request.user.district)
        return []


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthenticated,)


class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsSuperAdmin | IsImam | IsDeputy,)

    def delete(self, request, *args, **kwargs):
        if request.user == self.get_object().imam:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        return Response(status=403)


class BookUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    permission_classes = (IsSuperAdmin | IsImam | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)
