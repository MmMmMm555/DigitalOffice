# Generated by Django 4.1.13 on 2023-12-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firedefenceimages',
            name='type',
            field=models.CharField(choices=[(1, ''), (2, 'fire_safe'), (3, 'fire_closet'), (4, 'fires_ignal'), (5, 'auto_fire_extinguisher')], default=1, max_length=17),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_status',
            field=models.CharField(choices=[(1, 'good'), (2, 'repair'), (3, 'reconstruction')], max_length=17),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_type',
            field=models.CharField(choices=[(1, 'neighborhood'), (2, 'jome')], max_length=17),
        ),
    ]
