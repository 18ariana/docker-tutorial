# Generated by Django 3.0.4 on 2020-05-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0010_auto_20200517_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='image',
            field=models.ImageField(default='drivers/водитель1.jpeg', upload_to='drivers/', verbose_name='Изображение'),
        ),
    ]
