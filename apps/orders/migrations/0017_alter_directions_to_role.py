# Generated by Django 4.1.13 on 2024-01-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_directions_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='to_role',
            field=models.CharField(choices=[('2', 'Region Admin'), ('3', 'District Admin'), ('4', 'Imam'), ('5', 'Sub Imam'), ('6', 'Imam And Sub'), ('7', 'All')], default='4', max_length=18),
        ),
    ]
