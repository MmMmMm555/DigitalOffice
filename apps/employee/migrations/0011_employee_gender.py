# Generated by Django 4.1.13 on 2024-01-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_graduation_remove_employee_graduated_univer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=50),
        ),
    ]
