# Generated by Django 2.1.7 on 2019-02-19 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.IntegerField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=50, unique=True)),
                ('temperature', models.FloatField(max_length=10)),
                ('cloud_stat', models.CharField(max_length=50)),
                ('wind_speed', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField()),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_info_app.Region')),
            ],
        ),
    ]
