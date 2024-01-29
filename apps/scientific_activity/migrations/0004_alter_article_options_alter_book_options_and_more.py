# Generated by Django 4.1.13 on 2024-01-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_activity', '0003_alter_article_article_types_alter_article_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Maqola ', 'verbose_name_plural': 'Maqolalar '},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at'], 'verbose_name': 'Kitob ', 'verbose_name_plural': 'Kitoblar '},
        ),
        migrations.AlterField(
            model_name='book',
            name='comment',
            field=models.TextField(blank=True, verbose_name='comment'),
        ),
    ]
