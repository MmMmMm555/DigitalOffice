# Generated by Django 4.1.13 on 2023-12-14 07:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friday_tesis', '0006_remove_fridaytesisimamresult_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridaytesis',
            name='attachment',
            field=models.FileField(blank=True, help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/attachment', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt'])]),
        ),
        migrations.AlterField(
            model_name='fridaytesis',
            name='file',
            field=models.FileField(help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/fridaytesis', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt'])]),
        ),
        migrations.AlterField(
            model_name='fridaytesisimamresult',
            name='file',
            field=models.FileField(blank=True, help_text="allowed files: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt']", upload_to='files/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'zip', 'pptx', 'ppt'])]),
        ),
        migrations.AlterField(
            model_name='resultimages',
            name='image',
            field=models.ImageField(blank=True, help_text="allowed images: ['jpg', 'jpeg', 'png', 'svg']", upload_to='images/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])]),
        ),
        migrations.AlterField(
            model_name='resultvideos',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friday_tesis.fridaytesisimamresult', verbose_name='result_video'),
        ),
        migrations.AlterField(
            model_name='resultvideos',
            name='video',
            field=models.FileField(blank=True, help_text="allowed videos: ['mp4', 'mpeg', 'mpeg-4', 'm4v']", upload_to='videos/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mpeg', 'mpeg-4', 'm4v'])]),
        ),
    ]