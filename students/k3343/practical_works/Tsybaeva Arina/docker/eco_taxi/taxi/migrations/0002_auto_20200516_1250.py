# Generated by Django 3.0.4 on 2020-05-16 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cost',
        ),
        migrations.DeleteModel(
            name='CostFabric',
        ),
    ]
