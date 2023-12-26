from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

from apps.common.models import BaseModel
from apps.users.models import User


class Types(models.TextChoices):
    ELECTRON = '1'
    PRINT = '2'

class PublicationType(models.TextChoices):
    NEWSPAPER = '1'
    JOURNAL = '2'

class ArticleType(models.TextChoices):
    ISLAM_NURI = '1'
    HIDAYAT = '2'
    IMAM_BUKXARIY = '3'
    MUMINS = '4'
    OTHER = '5'


class Images(models.Model):
    image = models.ImageField(upload_to='images/article', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    class Meta: 
        verbose_name = 'Maqola rasmi '
        verbose_name_plural = 'Maqola rasmlari '


class Article(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_articles')
    type = models.CharField(max_length=22, choices=Types.choices, default=Types.PRINT, blank=False)
    comment = models.TextField()
    images = models.ManyToManyField(Images, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    publication = models.CharField(max_length=200, blank=True, null=True)
    publication_type = models.CharField(max_length=10, blank=True, null=True, choices=PublicationType.choices)
    article_types = models.CharField(max_length=15, blank=True, null=True, choices=ArticleType.choices)
    date = models.DateField()
    
    def __str__(self):
        return self.imam.username

    class Meta: 
        verbose_name = 'Maqola '
        verbose_name_plural = 'Maqolalar '



class Direction(models.TextChoices):
    RELIGIOUS = '1'
    EDUCATIONAL = '2'


class BookImages(models.Model):
    image = models.ImageField(upload_to='images/book', validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_TYPES)], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    class Meta: 
        verbose_name = 'Kitob rasmi '
        verbose_name_plural = 'Kitob rasmlari '


class Book(BaseModel):
    imam = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imam_books')
    name = models.CharField(max_length=200)
    images = models.ManyToManyField(BookImages, blank=True)
    direction = models.CharField(max_length=22, choices=Direction.choices, default=Direction.RELIGIOUS, blank=False)
    publication = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.imam.username

    class Meta: 
        verbose_name = 'Kitob '
        verbose_name_plural = 'Kitoblar '