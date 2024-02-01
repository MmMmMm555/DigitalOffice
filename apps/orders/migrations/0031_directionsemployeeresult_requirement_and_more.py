# Generated by Django 4.1 on 2024-02-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_alter_directionsemployeeread_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='directionsemployeeresult',
            name='requirement',
            field=models.BooleanField(default=False, verbose_name='requirement'),
        ),
        migrations.AddField(
            model_name='directionsemployeeresult',
            name='state',
            field=models.CharField(choices=[('unseen', 'Unseen'), ('accepted', 'Accepted'), ('done', 'Done'), ('delayed', 'Delayed')], default='unseen', max_length=10, verbose_name='state'),
        ),
        migrations.DeleteModel(
            name='DirectionsEmployeeRead',
        ),
    ]
