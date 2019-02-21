from django.db import models

# Create your models here.
class Region(models.Model):
    region_id = models.IntegerField()

    def __str__(self):
        return str(self.region_id)

class Weather(models.Model):
    region_id = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=10,decimal_places=1)
    cloud_desc = models.CharField(max_length=50)
    wind_speed = models.CharField(max_length=50)
    datetime = models.DateTimeField()

    class Meta:
        get_latest_by = "datetime"
