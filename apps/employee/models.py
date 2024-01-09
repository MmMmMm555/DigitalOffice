from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField
from django.conf import settings
from django.core.validators import FileExtensionValidator

from apps.mosque.models import Mosque

import uuid

# Create your models here.


class Education(models.TextChoices):
    MEDIUM_SPECIAL = '1'
    HIGH = '2'
    NONE = '3'


class Achievement(models.TextChoices):
    STATE_AWARDS = '1'
    COMMEMORATIVE_BADGES = '2'
    SIGNS = '3'
    GRATITUDE = '4'
    COMPLIMENT = '5'
    HONORARY_TITLES = '6'
    DIPLOMAS_OF_THE_WINNER_OF_THE_EXAM_COMPETITION = '7'
    DIPLOMAS_OF_COMPETITION_WINNERS = '8'
    INTERNATIONAL_AWARDS = '9'


class AcademicDegree(models.TextChoices):
    BACHELOR = '1'
    MASTER = '2'
    PhD = '3'
    DsC = '4'


class Nation(models.TextChoices):
    UZBEK = '1'
    RUSSIAN = '2'
    KAZAKH = '3'
    TAJIK = '4'
    TURKMEN = '5'


class Social(models.TextChoices):
    TELEGRAM = '1'
    INSTAGRAM = '2'
    FACEBOOK = '3'
    TIK_TOK = '4'
    TWITTER = '5'
    YOUTUBE = '6'
    WHATSAPP = '7'


class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'


class Graduation(models.Model):
    name = models.CharField(max_length=200, blank=False)


# class Graduation(models.TextChoices):
#     TASHKENT_ISLAMIC_INSTITUTE = '1'
#     SCHOOL_OF_HADITH_SCIENCE = '2'
#     MIR_ARAB_HIGHER_MADRASAH = '3'
#     KOKALDOSH = '4'
#     MIR_ARAB = '5'
#     KHOJA_BUKHARI = '6'
#     IMAM_TERMIZI = '7'
#     FAKHRIDDIN_AR_RAZI = '8'
#     MUHAMMAD_AL_BERUNI = '9'
#     SAYYID_MUHIDDIN_MAKHDUM = '10'
#     HIDAYAH = '11'
#     KHADICHAI_KUBRO = '12'
#     JOYBORI_KALON = '13'
#     ANOTHER = '14'


class Department(models.Model):
    name = models.CharField(max_length=200, blank=False)


class Position(models.Model):
    name = models.CharField(max_length=200, blank=False)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='position')


class Employee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, blank=True, editable=True)
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(blank=False, unique=True)
    address = PlainLocationField(based_fields=['city'], zoom=7)
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/profil_images/', default="images/default/default_user.jpg", validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True)
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=50, choices=Gender.choices, default=Gender.MALE)
    education = models.CharField(
        max_length=50, choices=Education.choices, blank=True)
    nation = models.CharField(
        max_length=10, choices=Nation.choices, blank=True, default=Nation.UZBEK)
    graduated_univer = models.ForeignKey(Graduation, on_delete=models.SET_NULL, blank=True, null=True)
    graduated_year = models.DateField(default="2000-01-01")
    diploma_number = models.CharField(max_length=20, blank=True)
    academic_degree = models.CharField(
        max_length=50, choices=AcademicDegree.choices, blank=True)
    achievement = models.CharField(
        max_length=50, choices=Achievement.choices, blank=True)
    mosque = models.ForeignKey(
        Mosque, on_delete=models.SET_NULL, null=True, related_name='employee', blank=True)

    class Meta:
        ordering = ['-id',]
        verbose_name = 'Hodim '
        verbose_name_plural = 'Hodimlar '

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


# class WorkActivity(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='workactivity')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     company = models.CharField(max_length=100, blank=True, null=True)
#     as_who = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         verbose_name = 'ish faoliyati '
#         verbose_name_plural = 'ish faoliyati '

#     def __str__(self) -> str:
#         return self.company


class SocialMedia(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='socialmedia')
    social_media = models.CharField(
        max_length=30, choices=Social.choices, blank=False)
    link = models.URLField(max_length=60, blank=False)

    class Meta:
        verbose_name = 'Ijtimoiy tarmoq '
        verbose_name_plural = 'Ijtimoiy tarmoq '

    def __str__(self) -> str:
        return self.social_media


# class Activity(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='activity')
#     type = models.CharField(max_length=1000, blank=True, null=True)
#     activity = models.CharField(max_length=1000, blank=True, null=True)
#     image = models.ImageField(upload_to='images/employee_activity/', default="default/no_photo.png")

#     class Meta:
#         verbose_name = 'tashabbusi '
#         verbose_name_plural = 'tashabbuslari '

#     def __str__(self) -> str:
#         return self.type
