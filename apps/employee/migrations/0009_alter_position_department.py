# Generated by Django 4.1.13 on 2024-01-07 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_department_employee_nation_alter_employee_mosque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='employee.department'),
        ),
    ]