from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date, datetime

from apps.friday_tesis import models
from apps.users.models import Role
from apps.orders.models import States
from apps.users.models import User
from apps.mosque.models import Mosque
# from apps.common.regions import Regions, Districts

from django.db import transaction


class FridayThesisSerializer(ModelSerializer):
    class Meta:
        model = models.FridayThesis
        fields = ('id',
                  'title',
                  'types',
                  'to_region',
                  'to_district',
                  'date',
                  'created_at',
                  'updated_at',
                  )
        depth = 1


class FridayThesisDetailSerializer(ModelSerializer):
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
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.to_mosque:
            representation['to_mosque'] = Mosque.objects.filter(
                id__in=instance.to_mosque.all()).values('id', 'name',)
        representation['waiting'] = models.FridayThesisImamRead.objects.filter(
            tesis=instance, state=States.UNSEEN).count()
        representation['accepted'] = models.FridayThesisImamRead.objects.filter(
            tesis=instance, state=States.ACCEPTED).count()
        representation['done'] = models.FridayThesisImamRead.objects.filter(
            tesis=instance, state=States.DONE).count()
        return representation


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
        with transaction.atomic():
            thesis = super().create(validated_data)
            imams = User.objects.filter(role=Role.IMAM)
            notifications_to_create = [models.FridayThesisImamRead(
                tesis=thesis,
                imam=i,
            ) for i in imams]
            models.FridayThesisImamRead.objects.bulk_create(
                notifications_to_create)
            seen = models.FridayThesisImamRead.objects.filter(tesis=thesis)

            mosque_list = thesis.to_mosque.all()
            district_list = thesis.to_district.all()
            region_list = thesis.to_region.all()

            if region_list:
                seen.filter(imam__in=imams.filter(
                    region__in=region_list)).update(requirement=True)
            if district_list:
                seen.filter(imam__in=imams.filter(
                    district__in=district_list)).update(requirement=True)
            if mosque_list:
                seen.filter(imam__in=imams.filter(
                    profil__mosque__in=mosque_list)).update(requirement=True)

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
                  #   'to_region',
                  #   'to_district',
                  #   'to_mosque',
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

    # def update(self, instance, validated_data):
        # try:

        # tesis = instance
        # instance.title = validated_data.get('title', instance.title)
        # instance.types = validated_data.get('types', instance.types)
        # instance.file = validated_data.get('file', instance.file)
        # instance.attachment = validated_data.get('attachment', instance.attachment)
        # instance.date = validated_data.get('date', instance.date)
        # instance.image = validated_data.get('image', instance.image)
        # instance.video = validated_data.get('video', instance.video)
        # instance.comment = validated_data.get('comment', instance.comment)
        # instance.file_bool = validated_data.get('file_bool', instance.file_bool)
        # instance.save()

        # models.FridayThesisImamRead.objects.filter(tesis=instance).update(seen=False)

        # imams = User.objects.filter(role='4')
        # print(instance.to_region)
        # print(validated_data.get('to_region'))
        # imam_list = validated_data.get('to_mosque', instance.to_mosque)
        # district_list = validated_data.get('to_district', instance.to_district)
        # region_list = validated_data.get('to_region', instance.to_region)
        # print(region_list)
        # imams = imams.filter(region__in=region_list)
        # region_list = Regions.objects.filter(name__in=region_list)

        # if not district_list:
        #     district_list = Districts.objects.filter(region__in=region_list)

        # if district_list:
        #     imams = imams.filter(district__in=district_list)

        # if imam_list:
        #     imams = imams.filter(username__in=imam_list)

        # seen = models.FridayThesisImamRead.objects.filter(tesis=instance, imam__in=imams,)
        # seen.update(requirement=True)

        # instance.to_mosque.clear()
        # instance.to_region.clear()
        # instance.to_district.clear()

        # instance.to_mosque.set(imams)
        # instance.to_region.set(region_list)
        # instance.to_district.set(district_list)
        # instance.save()

        # return instance
        # except:
        #     raise ValidationError('Something went wrong')
