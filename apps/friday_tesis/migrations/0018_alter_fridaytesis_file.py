# Generated by Django 4.1.13 on 2024-01-06 12:47

import apps.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friday_tesis', '0017_fridaytesis_attachment_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridaytesis',
            name='file',
            field=models.FileField(blank=True, help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/fridaytesis', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']), apps.common.validators.validate_file_size]),
        ),
    ]
