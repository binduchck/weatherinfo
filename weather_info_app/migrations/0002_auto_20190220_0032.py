# Generated by Django 2.1.7 on 2019-02-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_info_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region_id',
            field=models.IntegerField(unique=True),
        ),
    ]
