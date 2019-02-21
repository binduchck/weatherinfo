from rest_framework import routers
from weather_info_app.viewsets import WeatherViewSet


router = routers.DefaultRouter()
router.register(r'weather', WeatherViewSet)
