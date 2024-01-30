from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date, datetime
from django.db import transaction

from apps.friday_tesis import models
from apps.users.models import Role
from apps.orders.models import States
from apps.users.models import User
from apps.common.related_serializers import MosqueRelatedSerializer
from apps.common.api_endpoints.districts.serializers import RegionsSerializer
from apps.common.api_endpoints.regions.serializers import DistrictsSerializer
from apps.friday_tesis.tasks import create_thesis_notifications


class FridayThesisSerializer(ModelSerializer):
    to_region = RegionsSerializer(many=True, read_only=True)
    to_district = DistrictsSerializer(many=True, read_only=True)

    class Meta:
        model = models.FridayThesis
        fields = ('id',
                  'title',
                  'types',
                  'to_region',
                  'to_district',
                  'date',
                  'created_at',
                  )
        read_only_fields = fields


class FridayThesisDetailSerializer(ModelSerializer):
    to_region = RegionsSerializer(many=True, read_only=True)
    to_district = DistrictsSerializer(many=True, read_only=True)
    to_mosque = MosqueRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = models.FridayThesis
        fields = ('id',
                  'title',
                  'types',
                  'file',
                  'file_comment',
                  'attachment',
                  'attachment_comment',
                  'to_region',
                  'to_district',
                  'to_mosque',
                  'date',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  'created_at',
                  'updated_at',
                  )
        read_only_fields = fields


class FridayThesisCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FridayThesis
        fields = ('id',
                  'title',
                  'types',
                  'file',
                  'file_comment',
                  'attachment',
                  'attachment_comment',
                  'to_region',
                  'to_district',
                  'to_mosque',
                  'date',
                  'created_at',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )

    def create(self, validated_data):
        thesis = super().create(validated_data)
        # with transaction.atomic():
        task = create_thesis_notifications.delay(thesis=thesis.id)
        print(task.status)
        # imams = User.objects.filter(role=Role.IMAM)
        # notifications_to_create = [models.FridayThesisImamRead(
        #     tesis=thesis,
        #     imam=i,
        # ) for i in imams]
        # models.FridayThesisImamRead.objects.bulk_create(
        #     notifications_to_create)
        # seen = models.FridayThesisImamRead.objects.filter(tesis=thesis)

        # mosque_list = thesis.to_mosque.all()
        # district_list = thesis.to_district.all()
        # region_list = thesis.to_region.all()

        # if region_list:
        #     seen.filter(imam__in=imams.filter(
        #         region__in=region_list)).update(requirement=True)
        # if district_list:
        #     seen.filter(imam__in=imams.filter(
        #         district__in=district_list)).update(requirement=True)
        # if mosque_list:
        #     seen.filter(imam__in=imams.filter(
        #         profil__mosque__in=mosque_list)).update(requirement=True)

        return thesis


class FridayThesisUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.FridayThesis
        fields = ('id',
                  'title',
                  'types',
                  'file',
                  'file_comment',
                  'attachment',
                  'attachment_comment',
                  'date',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )
        extra_kwargs = {
            'title': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if self.instance.date <= date.today() or (self.instance.date == date.today() and int(datetime.now().hour) > 12):
            raise ValidationError('editable date passed')
        else:
            models.FridayThesisImamRead.objects.filter(
                tesis=self.instance).update(state=States.UNSEEN)
        return attrs
