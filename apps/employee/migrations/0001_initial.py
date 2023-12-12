# Generated by Django 4.1.13 on 2023-12-12 05:02

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mosque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', location_field.models.plain.PlainLocationField(max_length=63)),
                ('image', models.ImageField(default='default/default_user.png', upload_to='images/profil_images/')),
                ('birth_date', models.DateField()),
                ('education', models.CharField(blank=True, choices=[('1', 'Medium Special'), ('2', 'High'), ('3', 'None')], default='1', max_length=50)),
                ('graduated_univer', models.CharField(blank=True, choices=[('1', 'Tashkent Islamic Institute'), ('2', 'School Of Hadith Science'), ('3', 'Mir Arab Higher Madrasah'), ('4', 'Kokaldosh'), ('5', 'Mir Arab'), ('6', 'Khoja Bukhari'), ('7', 'Imam Termizi'), ('8', 'Fakhriddin Ar Razi'), ('9', 'Muhammad Al Beruni'), ('10', 'Sayyid Muhiddin Makhdum'), ('11', 'Hidayah'), ('12', 'Khadichai Kubro'), ('13', 'Joybori Kalon'), ('14', 'Another')], default='1', max_length=70)),
                ('graduated_year', models.DateField(blank=True)),
                ('diploma_number', models.CharField(blank=True, max_length=20)),
                ('academic_degree', models.CharField(blank=True, choices=[('1', 'Bachelor'), ('2', 'Master'), ('3', 'Phd'), ('4', 'Dsc')], default='1', max_length=50)),
                ('achievement', models.CharField(blank=True, choices=[('1', 'State Awards'), ('2', 'Commemorative Badges'), ('3', 'Signs'), ('4', 'Gratitude'), ('5', 'Compliment'), ('6', 'Honorary Titles'), ('7', 'Diplomas Of The Winner Of The Exam Competition'), ('8', 'Diplomas Of Competition Winners'), ('9', 'International Awards')], default='1', max_length=50)),
                ('mosque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='mosque.mosque')),
            ],
            options={
                'verbose_name': 'Hodim ',
                'verbose_name_plural': 'Hodimlar ',
            },
        ),
        migrations.CreateModel(
            name='WorkActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('as_who', models.CharField(blank=True, max_length=100, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workactivity', to='employee.employee')),
            ],
            options={
                'verbose_name': 'ish faoliyati ',
                'verbose_name_plural': 'ish faoliyati ',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(choices=[('1', 'Telegram'), ('2', 'Instagram'), ('3', 'Facebook'), ('4', 'Tik Tok'), ('5', 'Twitter'), ('6', 'Youtube'), ('7', 'Whatsapp')], default='1', max_length=30)),
                ('link', models.URLField(max_length=60)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialmedia', to='employee.employee')),
            ],
            options={
                'verbose_name': 'ijtimoiy tarmoq ',
                'verbose_name_plural': 'ijtimoiy tarmoq ',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(default='default/no_photo.png', upload_to='images/employee_activity/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='employee.employee')),
            ],
            options={
                'verbose_name': 'tashabbusi ',
                'verbose_name_plural': 'tashabbuslari ',
            },
        ),
    ]
