from django.apps import AppConfig


class WeatherAppConfig(AppConfig):
    name = 'weather_info_app'

    def ready(self):
        from weather_info_app import scheduler
        scheduler.start()
