from rest_framework import viewsets
from weather_info_app.models import Weather
from weather_info_app.serializer import WeatherSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
