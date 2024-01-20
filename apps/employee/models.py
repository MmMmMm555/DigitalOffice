from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from apps.common.validators import validate_image_size

from apps.mosque.models import Mosque


class Education(models.TextChoices):
    MEDIUM_SPECIAL = 'medium_special'  # o'rta maxsus
    HIGH = 'high'                      # oliy
    NONE = 'none'                      # yo'q


class Achievement(models.TextChoices):
    STATE_AWARDS = 'state_awards'
    COMMEMORATIVE_BADGES = 'commemorative_badges'
    SIGNS = 'signs'
    GRATITUDE = 'gratitude'
    COMPLIMENT = 'compliment'
    HONORARY_TITLES = 'honorary_titles'
    DIPLOMAS_OF_THE_WINNER_OF_THE_EXAM_COMPETITION = 'diplomas_of_the_winner_of_the_exam_competition'
    DIPLOMAS_OF_COMPETITION_WINNERS = 'diplomas_of_competition_winners'
    INTERNATIONAL_AWARDS = 'international_awards'


class AcademicDegree(models.TextChoices):
    BACHELOR = 'bachelor'
    MASTER = 'master'
    PhD = 'phd'
    DsC = 'dsc'
    NONE = 'none'


class Nation(models.TextChoices):
    UZBEK = 'uzbek'
    RUSSIAN = 'russian'
    KAZAKH = 'kazakh'
    TAJIK = 'tajik'
    TURKMEN = 'turkmen'


class Social(models.TextChoices):
    TELEGRAM = 'telegram'
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    TIK_TOK = 'tik_tok'
    TWITTER = 'twitter'
    YOUTUBE = 'youtube'
    WHATSAPP = 'whatsapp'


class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'


class Graduation(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Universitet '
        verbose_name_plural = 'Universitetlar '

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
    name = models.CharField(verbose_name=_("name"), max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Idora '
        verbose_name_plural = 'Idoralar '


class Position(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=200, blank=False)
    department = models.ForeignKey(
        Department, verbose_name=_("department"), on_delete=models.CASCADE, related_name='position')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lavozim '
        verbose_name_plural = 'Lavozimlar '


class Employee(models.Model):
    first_name = models.CharField(verbose_name=_("first_name"), max_length=50, blank=False)
    middle_name = models.CharField(verbose_name=_("middle_name"), max_length=50, blank=False)
    last_name = models.CharField(verbose_name=_("last_name"), max_length=50, blank=False)
    phone_number = PhoneNumberField(verbose_name=_("phone_number"), blank=False, unique=True)
    address = models.CharField(verbose_name=_("address"), max_length=200, blank=True)
    position = models.ForeignKey(
        Position, verbose_name=_("position"), on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(verbose_name=_("image"), upload_to='images/profil_images/', default="images/default/default_user.jpg", validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}", blank=True)
    birth_date = models.DateField(verbose_name=_("birth_date"), )
    gender = models.CharField(verbose_name=_("gender"), 
        max_length=50, choices=Gender.choices, default=Gender.MALE)
    education = models.CharField(verbose_name=_("education"), 
        max_length=50, choices=Education.choices, default=Education.NONE, blank=True)
    nation = models.CharField(verbose_name=_("nation"), 
        max_length=10, choices=Nation.choices, blank=True, default=Nation.UZBEK)
    graduated_univer = models.ForeignKey(
        Graduation, verbose_name=_("graduated_univer"), on_delete=models.SET_NULL, blank=True, null=True)
    graduated_year = models.DateField(verbose_name=_("graduated_year"), default="2000-01-01")
    diploma_number = models.CharField(verbose_name=_("diploma_number"), max_length=20, blank=True)
    academic_degree = models.CharField(verbose_name=_("academic_degree"), 
        max_length=50, choices=AcademicDegree.choices, default=AcademicDegree.NONE, blank=True)
    achievement = models.CharField(verbose_name=_("achievement"), 
        max_length=50, choices=Achievement.choices, blank=True)
    mosque = models.ForeignKey(
        Mosque, verbose_name=_("mosque"), on_delete=models.SET_NULL, null=True, related_name='employee', blank=True)

    class Meta:
        ordering = ['-id',]
        verbose_name = 'Xodim '
        verbose_name_plural = 'Xodimlar '

    def __str__(self) -> str:
        return f"{self.id} - {self.first_name}"


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
        Employee, verbose_name=_("employee"), on_delete=models.CASCADE, related_name='socialmedia')
    social_media = models.CharField(verbose_name=_("social_media"), 
        max_length=30, choices=Social.choices, blank=False)
    link = models.URLField(verbose_name=_("link"), max_length=60, blank=False)

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
