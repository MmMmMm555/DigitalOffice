# Generated by Django 4.1.13 on 2023-12-09 12:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friday_tesis', '0002_fridaytesis_created_at_fridaytesis_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridaytesis',
            name='to_district',
            field=models.ManyToManyField(blank=True, to='common.districts'),
        ),
        migrations.AddField(
            model_name='fridaytesis',
            name='to_region',
            field=models.ManyToManyField(to='common.regions'),
        ),
        migrations.AlterField(
            model_name='fridaytesis',
            name='attachment',
            field=models.FileField(blank=True, upload_to='files/attachment', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'xls', 'txt'])]),
        ),
        migrations.AlterField(
            model_name='fridaytesis',
            name='file',
            field=models.FileField(upload_to='files/fridaytesis', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'xls', 'txt'])]),
        ),
        migrations.AlterField(
            model_name='fridaytesis',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='fridaytesis',
            name='to_imams',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FridayTesisReqiredFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty', models.BooleanField(default=False)),
                ('image', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('comment', models.BooleanField(default=False)),
                ('file', models.BooleanField(default=False)),
                ('tesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requiredfields', to='friday_tesis.fridaytesis')),
                ('to_district', models.ManyToManyField(to='common.districts')),
                ('to_imams', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('to_region', models.ManyToManyField(to='common.regions')),
            ],
        ),
    ]
