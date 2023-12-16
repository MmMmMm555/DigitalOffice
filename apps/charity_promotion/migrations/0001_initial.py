# Generated by Django 4.1.13 on 2023-12-16 05:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharityPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('types', models.CharField(choices=[('1', 'Building'), ('2', 'Water Discharge'), ('3', 'Other')], default='1', max_length=22)),
                ('participant', models.CharField(choices=[('1', 'Initiative'), ('2', 'Participant'), ('3', 'Other')], default='1', max_length=22)),
                ('help_type', models.CharField(choices=[('1', 'Money'), ('2', 'Food'), ('3', 'Closes'), ('4', 'Medicine'), ('5', 'Other')], max_length=22)),
                ('from_who', models.CharField(choices=[('1', 'Mosque'), ('2', 'Sponsor'), ('3', 'Zakat'), ('4', 'Fidya'), ('5', 'Fitr'), ('6', 'Other')], max_length=22)),
                ('comment', models.TextField()),
                ('date', models.DateField()),
                ('imam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imam_charity_promotion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hayriya aksiyasi ',
                'verbose_name_plural': 'Hayriya aksiyalari ',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text="allowed images: ['jpg', 'jpeg', 'png', 'svg']", upload_to='images/charity_promotion/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg'])])),
                ('charity_promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='charity_promotion.charitypromotion')),
            ],
            options={
                'verbose_name': 'Hayriya aksiya rasmi ',
                'verbose_name_plural': 'Hayriya aksiya rasmilari ',
            },
        ),
    ]
