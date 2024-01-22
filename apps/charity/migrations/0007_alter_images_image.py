# Generated by Django 4.1.13 on 2024-01-20 09:18

import apps.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_alter_charity_comment_alter_charity_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(help_text="allowed images: ['jpg', 'jpeg', 'png', 'svg']", upload_to='images/charity/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg']), apps.common.validators.validate_image_size], verbose_name='image'),
        ),
    ]