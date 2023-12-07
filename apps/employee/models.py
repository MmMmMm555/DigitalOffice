from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField


# Create your models here.

class Education(models.TextChoices):
    MEDIUM_SPECIAL = "O'RTA MAXSUS"
    HIGH = "OLIY"
    NONE = "MALUMOTSIZ"

class Achievement(models.TextChoices):
    STATE_AWARDS = "Davlat mukofotlari"
    COMMEMORATIVE_BADGES = "Esdalik nishonlari"
    SIGNS = "Belgilar"
    GRATITUDE = "Minnatdorchilik"
    COMPLIMENT = "Maqtov"
    HONORARY_TITLES = "Faxriy unvonlar"
    DIPLOMAS_OF_THE_WINNER_OF_THE_EXAM_COMPETITION = "imtihon tanlovi g'olibining diplomlari"
    DIPLOMAS_OF_COMPETITION_WINNERS = "tanlov g‘oliblarining diplomlari"
    INTERNATIONAL_AWARDS = "xalqaro mukofotlar"

class AcademicDegree(models.TextChoices):
    BACHELOR = "Bakalavr"
    MASTER = "Magistr"
    PhD = "Doktorant"
    DsC = "Doktor"

class Social(models.TextChoices):
    TELEGRAM = "Telegram"
    INSTAGRAM = "Instagram"
    FACEBOOK = "Facebook"
    TIK_TOK = "Tik Tok"
    TWITTER = "Twitter"
    YOUTUBE = "YouTube"
    WHATSAPP = "WhatsApp"

class Graduation(models.TextChoices):
    TASHKENT_ISLAMIC_INSTITUTE = "Toshkent islom instituti"
    SCHOOL_OF_HADITH_SCIENCE = "Hadis ilmi maktabi"
    MIR_ARAB_HIGHER_MADRASAH = "Mir Arab Oliy Madrasasi"
    KOKALDOSH = "Ko'kaldosh"
    MIR_ARAB = "Mir Arab"
    KHOJA_BUKHARI = "Xoja Buxoriy"
    IMAM_TERMIZI = "Imom Termiziy"
    FAKHRIDDIN_AR_RAZI = "Faxriddin ar-Roziy"
    MUHAMMAD_AL_BERUNI = "Muhammad al-Beruniy"
    SAYYID_MUHIDDIN_MAKHDUM = "Sayyid Muhiddin Maxdum"
    HIDAYAH = "Hidoya"
    KHADICHAI_KUBRO = "Xadichai Kubro"
    JOYBORI_KALON = "Jo'ybori kalon"
    ANOTHER = "Boshqa"    


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(blank=False)
    address = PlainLocationField(based_fields=['city'], zoom=7)
    image = models.ImageField(upload_to='images/profil_images/', default="default/default_user.png")
    birth_date = models.DateField()
    education = models.CharField(max_length=50, choices=Education.choices, default=Education.MEDIUM_SPECIAL, blank=True)
    graduated_univer = models.CharField(max_length=70, choices=Graduation.choices, default=Graduation.TASHKENT_ISLAMIC_INSTITUTE, blank=True)
    graduated_year = models.DateField(blank=True)
    diploma_number = models.IntegerField(blank=True)
    academic_degree = models.CharField(max_length=50, choices=AcademicDegree.choices, default=AcademicDegree.BACHELOR, blank=True)
    achievement = models.CharField(max_length=50, choices=Achievement.choices, default=Achievement.STATE_AWARDS, blank=True)

    class Meta:
        verbose_name = 'Hodim '
        verbose_name_plural = 'Hodimlar '
    
    def __str__(self) -> str:
        return self.name


class WorkActivity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='workactivity')
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=100, blank=True, null=True)
    as_who = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'ish faoliyati '
        verbose_name_plural = 'ish faoliyati '
    
    def __str__(self) -> str:
        return self.company


class SocialMedia(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='socialmedia')
    social_media = models.CharField(max_length=30 , choices=Social.choices, default=Social.TELEGRAM)
    link = models.URLField(max_length=60)
    
    class Meta:
        verbose_name = 'ijtimoiy tarmoq '
        verbose_name_plural = 'ijtimoiy tarmoq '
    
    def __str__(self) -> str:
        return self.social_media


class Activity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='activity')
    type = models.CharField(max_length=1000, blank=True, null=True)
    activity = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/employee_activity/', default="default/no_photo.png")

    class Meta:
        verbose_name = 'tashabbusi '
        verbose_name_plural = 'tashabbuslari '

    def __str__(self) -> str:
        return self.type