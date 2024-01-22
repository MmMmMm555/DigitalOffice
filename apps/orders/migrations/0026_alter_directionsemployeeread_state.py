# Generated by Django 4.1.13 on 2024-01-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_alter_directions_to_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directionsemployeeread',
            name='state',
            field=models.CharField(choices=[('unseen', 'Unseen'), ('accepted', 'Accepted'), ('done', 'Done')], default='unseen', max_length=10),
        ),
    ]
