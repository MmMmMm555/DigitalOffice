# Generated by Django 4.1.13 on 2023-12-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0004_alter_attribute_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='type',
            field=models.CharField(choices=[('button', 'Button'), ('text', 'Text'), ('select', 'Select'), ('multiselect', 'Multiselect')], default='text', max_length=255),
        ),
    ]
