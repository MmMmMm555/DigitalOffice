# Generated by Django 4.1.13 on 2023-12-11 07:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=1000)),
                ('direction_type', models.CharField(choices=[('1', 'Decision'), ('2', 'Order'), ('3', 'Program'), ('4', 'Message'), ('5', 'Mission')], default='2', max_length=11)),
                ('file', models.FileField(upload_to='files/direction', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])),
                ('type', models.CharField(choices=[('1', 'Decision'), ('2', 'Order'), ('3', 'Program'), ('4', 'Message'), ('5', 'Mission')], default='1', max_length=12)),
                ('to_role', models.CharField(choices=[('1', 'Super Admin'), ('2', 'Region Admin'), ('3', 'District Admin'), ('4', 'Imam'), ('5', 'Sub Imam')], default='4', max_length=18)),
                ('from_date', models.DateField(blank=True)),
                ('to_date', models.DateField(blank=True)),
                ('voice', models.BooleanField(default=False)),
                ('image', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('comment', models.BooleanField(default=False)),
                ('file_bool', models.BooleanField(default=False)),
                ('to_district', models.ManyToManyField(blank=True, related_name='direction', to='common.districts')),
                ('to_imams', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('to_region', models.ManyToManyField(related_name='direction', to='common.regions')),
            ],
            options={
                'verbose_name': 'Buyruq ',
                'verbose_name_plural': 'Buyruqlar ',
            },
        ),
        migrations.CreateModel(
            name='DirectionsEmployeeRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('seen', models.BooleanField(default=False)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directionemployeeread', to='orders.directions')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directionemployeeread', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Buyruq oqilishi ',
                'verbose_name_plural': 'Buyruq oqilishlari ',
            },
        ),
        migrations.CreateModel(
            name='DirectionsEmployeeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('image', models.ImageField(blank=True, upload_to='images/directionsresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg'])])),
                ('video', models.FileField(blank=True, upload_to='videos/directionresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('voice', models.FileField(blank=True, upload_to='voices/directionresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])])),
                ('comment', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='files/directionresult', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'xls', 'txt', 'zip'])])),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directionemployeeresult', to='orders.directions')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directionemployeeresult', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Buyruq natija ',
                'verbose_name_plural': 'Buyruq natijalari ',
            },
        ),
        migrations.RemoveField(
            model_name='ordersemployeeread',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='ordersemployeeread',
            name='order',
        ),
        migrations.RemoveField(
            model_name='ordersemployeeresult',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='ordersemployeeresult',
            name='order',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrdersEmployeeRead',
        ),
        migrations.DeleteModel(
            name='OrdersEmployeeResult',
        ),
    ]