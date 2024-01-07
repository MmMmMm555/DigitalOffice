# Generated by Django 4.1.13 on 2024-01-07 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mosque', '0007_mosque_image'),
        ('employee', '0007_alter_employee_image_alter_employee_mosque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='nation',
            field=models.CharField(blank=True, choices=[('1', 'Uzbek'), ('2', 'Russian'), ('3', 'Kazakh'), ('4', 'Tajik'), ('5', 'Turkmen')], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mosque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='mosque.mosque'),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.position'),
        ),
    ]