from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from apps.common.validators import validate_image_size
from apps.common.models import BaseModel
from apps.users.models import User


class Types(models.TextChoices):
    ELECTRON = 'electron'
    PRINT = 'print'


class PublicationType(models.TextChoices):
    NEWSPAPER = 'newspaper'
    JOURNAL = 'journal'


class ArticleType(models.TextChoices):
    ISLAM_NURI = 'islam_nuri'
    HIDAYAT = 'hidayat'
    IMAM_BUKXARIY = 'imam_bukxariy'
    MUMINS = 'mumins'
    OTHER = 'other'


class Images(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/article', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    def __str__(self) -> str:
        return self.image.url

    class Meta:
        verbose_name = 'Maqola rasmi '
        verbose_name_plural = 'Maqola rasmlari '


class Article(BaseModel):
    imam = models.ForeignKey(
        User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='imam_articles')
    type = models.CharField(verbose_name=_("type"), 
        max_length=22, choices=Types.choices, default=Types.PRINT, blank=False)
    comment = models.TextField(verbose_name=_("comment"), )
    images = models.ManyToManyField(Images, verbose_name=_("images"), blank=True)
    url = models.URLField(verbose_name=_("url"), max_length=200, null=True, blank=True)
    publication = models.CharField(verbose_name=_("publication"), max_length=200, blank=True, null=True)
    publication_type = models.CharField(verbose_name=_("publication_type"), 
        max_length=10, blank=True, null=True, choices=PublicationType.choices)
    article_types = models.CharField(verbose_name=_("article_types"), 
        max_length=15, blank=True, null=True, choices=ArticleType.choices)
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return self.imam.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Maqola '
        verbose_name_plural = 'Maqolalar '


class Direction(models.TextChoices):
    RELIGIOUS = 'religious'
    EDUCATIONAL = 'educational'


class BookImages(models.Model):
    image = models.ImageField(verbose_name=_("image"), upload_to='images/book', validators=[FileExtensionValidator(
        allowed_extensions=settings.ALLOWED_IMAGE_TYPES), validate_image_size], help_text=f"allowed images: {settings.ALLOWED_IMAGE_TYPES}")

    class Meta:
        verbose_name = 'Kitob rasmi '
        verbose_name_plural = 'Kitob rasmlari '


class Book(BaseModel):
    imam = models.ForeignKey(
        User, verbose_name=_("imam"), on_delete=models.CASCADE, related_name='imam_books')
    name = models.CharField(verbose_name=_("name"), max_length=200)
    images = models.ManyToManyField(BookImages, verbose_name=_("images"), blank=True)
    direction = models.CharField(verbose_name=_("direction"), 
        max_length=22, choices=Direction.choices, default=Direction.RELIGIOUS, blank=False)
    publication = models.CharField(verbose_name=_("publication"), max_length=200, blank=True, null=True)
    comment = models.TextField(verbose_name=_("comment"), blank=True)
    date = models.DateField(verbose_name=_("date"), )

    def __str__(self):
        return self.imam.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Kitob '
        verbose_name_plural = 'Kitoblar '
