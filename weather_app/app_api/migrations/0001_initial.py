# Generated by Django 4.2.2 on 2023-08-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temp', models.IntegerField()),
                ('temp_max', models.IntegerField()),
                ('temp_min', models.IntegerField()),
                ('feels_like', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('wind', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]