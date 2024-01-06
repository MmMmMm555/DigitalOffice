# Generated by Django 4.1.13 on 2024-01-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0005_mosque_capacity_mosque_emergency_exit_door_and_more'),
        ('orders', '0018_alter_directions_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='required_to_employee',
            field=models.ManyToManyField(blank=True, to='mosque.mosque'),
        ),
        migrations.AlterField(
            model_name='directions',
            name='to_employee',
            field=models.ManyToManyField(blank=True, related_name='direction', to='mosque.mosque'),
        ),
    ]