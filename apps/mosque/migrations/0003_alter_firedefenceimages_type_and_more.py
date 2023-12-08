# Generated by Django 4.1.13 on 2023-12-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0002_alter_firedefenceimages_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firedefenceimages',
            name='type',
            field=models.CharField(choices=[(1, 'Evacuation Road'), (2, 'Fire Safe'), (3, 'Fire Closet'), (4, 'Fires Ignal'), (5, 'Auto Fire Extinguisher')], default=1, max_length=17),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_status',
            field=models.CharField(choices=[(1, 'Good'), (2, 'Repair'), (3, 'Reconstruction')], max_length=17),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_type',
            field=models.CharField(choices=[(1, 'Neighborhood'), (2, 'Jome')], max_length=17),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='other_room_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
