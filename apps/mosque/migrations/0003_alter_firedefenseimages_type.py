# Generated by Django 4.1.13 on 2023-12-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0002_rename_firedefenceimages_firedefenseimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firedefenseimages',
            name='type',
            field=models.CharField(choices=[('1', 'Evacuation Road'), ('2', 'Fire Safe'), ('3', 'Fire Closet'), ('4', 'Fire Signal'), ('5', 'Auto Fire Extinguisher')], default='1', max_length=17),
        ),
    ]
