# Generated by Django 4.1.13 on 2023-12-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_district_user_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('1', 'Super Admin'), ('2', 'Region Admin'), ('3', 'District Admin'), ('4', 'Imam'), ('5', 'Sub Imam')], default='4', max_length=18, null=True),
        ),
    ]
