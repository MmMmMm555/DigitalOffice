# Generated by Django 4.1.13 on 2023-12-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_directions_from_date_alter_directions_to_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='directions',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
