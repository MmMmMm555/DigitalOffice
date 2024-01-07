# Generated by Django 4.1.13 on 2024-01-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0005_mosque_capacity_mosque_emergency_exit_door_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mosque',
            name='graveyard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mosque',
            name='shop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mosque',
            name='shrine',
            field=models.BooleanField(default=False),
        ),
    ]