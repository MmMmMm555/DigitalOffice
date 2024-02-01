# Generated by Django 4.1 on 2024-02-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0012_remove_mosque_basement_remove_mosque_second_floor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mosque',
            name='floor',
        ),
        migrations.AddField(
            model_name='mosque',
            name='basement',
            field=models.BooleanField(default=False, verbose_name='basement'),
        ),
        migrations.AddField(
            model_name='mosque',
            name='second_floor',
            field=models.BooleanField(default=False, verbose_name='second_floor'),
        ),
        migrations.AddField(
            model_name='mosque',
            name='third_floor',
            field=models.BooleanField(default=False, verbose_name='third_floor'),
        ),
    ]
