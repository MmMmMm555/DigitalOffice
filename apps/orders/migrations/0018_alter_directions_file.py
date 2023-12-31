# Generated by Django 4.1.13 on 2024-01-06 06:43

import apps.common.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_directions_to_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='file',
            field=models.FileField(blank=True, help_text="allowed files : ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/direction', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']), apps.common.validators.validate_file_size]),
        ),
    ]
