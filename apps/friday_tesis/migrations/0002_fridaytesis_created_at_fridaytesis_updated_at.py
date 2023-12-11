# Generated by Django 4.1.13 on 2023-12-09 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('friday_tesis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridaytesis',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridaytesis',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated date'),
        ),
    ]