from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     UpdateAPIView, RetrieveAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (BookSerializer, BookListSerializer,
                          BookUpdateSerializer, BookDetailSerializer,)
from apps.scientific_activity.models import Book
from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.common.view_mixin import FilerQueryByRole


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class BookListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Book.objects.only(
        'id', 'imam', 'name', 'direction', 'date',).select_related('imam', 'imam__profil',)
    serializer_class = BookListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'direction', 'date', 'created_at',)


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthenticated,)


class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)
