# Generated by Django 4.1.13 on 2023-12-08 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('mosque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='mosque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='mosque.mosque'),
        ),
        migrations.AddField(
            model_name='activity',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='employee.employee'),
        ),
    ]