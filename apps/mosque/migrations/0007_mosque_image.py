# Generated by Django 4.1.13 on 2024-01-06 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0006_mosque_graveyard_mosque_shop_mosque_shrine'),
    ]

    operations = [
        migrations.AddField(
            model_name='mosque',
            name='image',
            field=models.ImageField(blank=True, default='images/default/default_mosque.png', help_text="allowed images: ['jpg', 'jpeg', 'png', 'svg']", upload_to='images/mosque/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])]),
        ),
    ]
