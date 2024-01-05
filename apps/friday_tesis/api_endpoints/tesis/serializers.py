from rest_framework.serializers import ModelSerializer, ValidationError, ManyRelatedField
from datetime import date, datetime

from apps.friday_tesis import models
from apps.users.models import User
from apps.common.regions import Regions, Districts


class FridayTesisSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesis
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


class FridayTesisDetailSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesis
        fields = ('id',
                  'title',
                  'types',
                  'file',
                  'file_comment',
                  'attachment',
                  'attachment_comment',
                  'to_region',
                  'to_district',
                  'to_imams',
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
        if instance.to_imams:
            representation['to_imams'] = User.objects.filter(
                id__in=instance.to_imams.all()).values('id', 'profil__name', 'profil__last_name',)
        representation['waiting'] = models.FridayTesisImamRead.objects.filter(
            tesis=instance, state='1').count()
        representation['accepted'] = models.FridayTesisImamRead.objects.filter(
            tesis=instance, state='2').count()
        representation['done'] = models.FridayTesisImamRead.objects.filter(
            tesis=instance, state='3').count()
        return representation


class FridayTesisCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesis
        fields = ('id',
                  'title',
                  'types',
                  'file',
                  'file_comment',
                  'attachment',
                  'attachment_comment',
                  'to_region',
                  'to_district',
                  'to_imams',
                  'date',
                  'created_at',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )

    def create(self, validated_data):
        try:
            tesis = models.FridayTesis.objects.create(
                title=validated_data.get('title', None),
                types=validated_data.get('types', None),
                file=validated_data.get('file', None),
                file_comment=validated_data.get('file_comment', None),
                attachment=validated_data.get('attachment', None),
                attachment_comment=validated_data.get('attachment_comment', None),
                date=validated_data.get('date', None),
                image=validated_data.get('image', None),
                video=validated_data.get('video', None),
                comment=validated_data.get('comment', None),
                file_bool=validated_data.get('file_bool', None),
            )

            imams = User.objects.filter(role='4')

            for i in imams:
                models.FridayTesisImamRead.objects.create(
                    tesis=tesis,
                    imam=i,
                )

            imam_list = validated_data.get('to_imams', [])
            district_list = validated_data.get('to_district', [])
            region_list = validated_data.get('to_region', [])
            if region_list == []:
                region_list = Regions.objects.all()
            imams = imams.filter(region__in=region_list)
            # region_list = Regions.objects.filter(name__in=region_list)

            if not district_list:
                district_list = Districts.objects.filter(
                    region__in=region_list)

            if district_list:
                imams = imams.filter(district__in=district_list)

            if imam_list:
                imams = imams.filter(username__in=imam_list)

            seen = models.FridayTesisImamRead.objects.filter(
                tesis=tesis, imam__in=imams,)
            seen.update(requirement=True)

            tesis.to_imams.set(imams)
            tesis.to_region.set(region_list)
            tesis.to_district.set(district_list)
            tesis.save()

            return tesis
        except:
            tesis.delete()
            raise ValidationError('Something went wrong')


class FridayTesisUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesis
        fields = ('id',
                  'title',
                  'types',
                  'file',
                  'file_comment',
                  'attachment',
                  'attachment_comment',
                  #   'to_region',
                  #   'to_district',
                  #   'to_imams',
                  'date',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )
        extra_kwargs = {
            'title': {'required': False},
            'file': {'required': False},
            'date': {'required': False},
        }

    def save(self):
        if self.instance.date <= date.today() or (self.instance.date == date.today() and int(datetime.now().hour) > 13):
            raise ValidationError('editable date passed')
        obj = models.FridayTesis.objects.filter(
            id=self.instance.id).update(**self.validated_data)
        models.FridayTesisImamRead.objects.filter(
            tesis=self.instance).update(state='1')
        return obj

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

        # models.FridayTesisImamRead.objects.filter(tesis=instance).update(seen=False)

        # imams = User.objects.filter(role='4')
        # print(instance.to_region)
        # print(validated_data.get('to_region'))
        # imam_list = validated_data.get('to_imams', instance.to_imams)
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

        # seen = models.FridayTesisImamRead.objects.filter(tesis=instance, imam__in=imams,)
        # seen.update(requirement=True)

        # instance.to_imams.clear()
        # instance.to_region.clear()
        # instance.to_district.clear()

        # instance.to_imams.set(imams)
        # instance.to_region.set(region_list)
        # instance.to_district.set(district_list)
        # instance.save()

        # return instance
        # except:
        #     raise ValidationError('Something went wrong')
