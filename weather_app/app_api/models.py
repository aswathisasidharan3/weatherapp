from django.db import models

# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temp = models.IntegerField()
    temp_max = models.IntegerField()
    temp_min = models.IntegerField()
    feels_like = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    wind = models.IntegerField()
    description = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


