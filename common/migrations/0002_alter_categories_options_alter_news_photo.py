# Generated by Django 5.1.7 on 2025-03-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'CATEGORIES', 'verbose_name_plural': 'CATEGORIESES'},
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
