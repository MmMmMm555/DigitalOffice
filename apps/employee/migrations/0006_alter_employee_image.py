# Generated by Django 4.1.13 on 2024-01-06 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='images/default/default_user.png', help_text="allowed images: ['jpg', 'jpeg', 'png', 'svg']", upload_to='images/profil_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])]),
        ),
    ]