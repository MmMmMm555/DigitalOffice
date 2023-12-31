# Generated by Django 4.1.13 on 2023-12-12 05:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FridayTesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to='files/fridaytesis', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])),
                ('attachment', models.FileField(blank=True, upload_to='files/attachment', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])),
                ('date', models.DateField()),
                ('image', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('comment', models.BooleanField(default=False)),
                ('file_bool', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Juma tezisi ',
                'verbose_name_plural': 'Juma tezislari ',
            },
        ),
        migrations.CreateModel(
            name='FridayTesisImamRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('seen', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Juma tezisi imom oqigan ',
                'verbose_name_plural': 'Juma tezislari imom oqiganlar ',
            },
        ),
        migrations.CreateModel(
            name='FridayTesisImamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('image', models.ImageField(blank=True, upload_to='images/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg'])])),
                ('video', models.FileField(blank=True, upload_to='videos/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('comment', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='files/tesisresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])),
            ],
            options={
                'verbose_name': 'Juma tezisi imom natija ',
                'verbose_name_plural': 'Juma tezislari imom natijalar ',
            },
        ),
    ]
