# Generated by Django 4.1.13 on 2024-01-22 10:30

import apps.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marriage', '0004_alter_marriage_options_alter_marriage_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marriage',
            name='fhdyo_document',
        ),
        migrations.RemoveField(
            model_name='marriage',
            name='marriage_document',
        ),
        migrations.AlterField(
            model_name='marriage',
            name='marriage_image',
            field=models.FileField(help_text="allowed images: ['jpg', 'jpeg', 'png', 'svg']", upload_to='images/marriage_images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg']), apps.common.validators.validate_image_size], verbose_name='marriage_image'),
        ),
    ]
