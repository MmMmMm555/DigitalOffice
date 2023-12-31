# Generated by Django 4.1.13 on 2023-12-19 10:13

import apps.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friday_tesis', '0013_remove_fridaytesisimamread_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridaytesis',
            name='attachment',
            field=models.FileField(blank=True, help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/attachment', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']), apps.common.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='fridaytesis',
            name='file',
            field=models.FileField(help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/fridaytesis', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']), apps.common.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='fridaytesisimamresult',
            name='file',
            field=models.FileField(blank=True, help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']), apps.common.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='resultvideos',
            name='video',
            field=models.FileField(blank=True, help_text="allowed videos: ['mp4', 'mpeg', 'mpeg-4', 'm4v']", upload_to='videos/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mpeg', 'mpeg-4', 'm4v']), apps.common.validators.validate_file_size]),
        ),
    ]
