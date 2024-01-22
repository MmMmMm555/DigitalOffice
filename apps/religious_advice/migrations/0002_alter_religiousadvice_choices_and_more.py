# Generated by Django 4.1.13 on 2024-01-22 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('religious_advice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='religiousadvice',
            name='choices',
            field=models.CharField(choices=[('prayers', 'Prayers'), ('spleen', 'Spleen'), ('commerce', 'Commerce'), ('debt', 'Debt'), ('heritage', 'Heritage'), ('faith', 'Faith'), ('jihad', 'Jihad'), ('takfir', 'Takfir'), ('vasiyla', 'Vasiyla'), ('other0', 'Other')], max_length=12, verbose_name='choices'),
        ),
        migrations.AlterField(
            model_name='religiousadvice',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='religiousadvice',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='religiousadvice',
            name='imam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imam_religious_advice', to=settings.AUTH_USER_MODEL, verbose_name='imam'),
        ),
        migrations.AlterField(
            model_name='religiousadvice',
            name='type',
            field=models.CharField(choices=[('fiqh', 'Fiqh'), ('creed', 'Creed'), ('other', 'Other')], default='other', max_length=12, verbose_name='type'),
        ),
    ]
