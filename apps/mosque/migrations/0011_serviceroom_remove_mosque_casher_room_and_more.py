# Generated by Django 4.1 on 2024-02-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0010_alter_firedefenseimages_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('name', models.CharField(max_length=110, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Xizmat xona ',
                'verbose_name_plural': 'Xizmat xonalar ',
            },
        ),
        migrations.RemoveField(
            model_name='mosque',
            name='casher_room',
        ),
        migrations.RemoveField(
            model_name='mosque',
            name='guard_room',
        ),
        migrations.RemoveField(
            model_name='mosque',
            name='imam_room',
        ),
        migrations.RemoveField(
            model_name='mosque',
            name='other_room',
        ),
        migrations.RemoveField(
            model_name='mosque',
            name='other_room_amount',
        ),
        migrations.RemoveField(
            model_name='mosque',
            name='sub_imam_room',
        ),
        migrations.AlterField(
            model_name='firedefenseimages',
            name='type',
            field=models.CharField(choices=[('evacuation_road', 'evacuation_road'), ('fire_safe', 'fire_safe'), ('fire_closet', 'fire_closet'), ('fire_signal', 'fire_signal'), ('auto_fire_extinguisher', 'auto_fire_extinguisher'), ('emergency_exit_door', 'emergency_exit_door')], default='evacuation_road', max_length=22, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_heating_fuel',
            field=models.CharField(blank=True, choices=[('gas', 'gas'), ('liquid_fuel', 'liquid_fuel'), ('solid_fuel', 'solid_fuel'), ('none', 'none')], max_length=17, verbose_name='mosque_heating_fuel'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_heating_type',
            field=models.CharField(blank=True, choices=[('central', 'central'), ('local', 'local')], max_length=17, verbose_name='mosque_heating_type'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_status',
            field=models.CharField(choices=[('good', 'good'), ('repair', 'repair'), ('reconstruction', 'reconstruction')], default='good', max_length=17, verbose_name='mosque_status'),
        ),
        migrations.AlterField(
            model_name='mosque',
            name='mosque_type',
            field=models.CharField(choices=[('neighborhood', 'neighborhood'), ('jame', 'jame')], default='jame', max_length=17, verbose_name='mosque_type'),
        ),
        migrations.AddField(
            model_name='mosque',
            name='service_rooms',
            field=models.ManyToManyField(blank=True, to='mosque.serviceroom', verbose_name='service_rooms'),
        ),
    ]