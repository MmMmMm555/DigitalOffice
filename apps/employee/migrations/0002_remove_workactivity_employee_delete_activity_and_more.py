# Generated by Django 4.1.13 on 2023-12-13 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workactivity',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='WorkActivity',
        ),
    ]
