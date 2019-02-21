#from django_cron import CronJobBase, Schedule
from weather_info_app.models import Region, Weather
from apscheduler.schedulers.background import BackgroundScheduler
from weatherinfo import settings
import requests
import configparser
import datetime
import logging

log = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read(settings.CONFIG)

def get_weather_info():

    # TODO These needs to be set in config
    url = config.get(API_URL)
    headers = {
        'x-api-key' : config.get(API_KEY)
    }
    querystring = config.get(API_QUERY_STRING)
    try:
        response = requests.get(url, headers=headers, params=querystring)
    except Exception as ex:
        log.error("Exception occured {}".format(ex))
        raise
    log.info('Response Code : {}'.format(response.status_code))
    return response.json()

def populate_weather_info():
    # hit weather api and gather info
    data = get_weather_info()
    temp = data['main']['temp'] - 273.15
    date_time = datetime.datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d')
    cloud_desc = data['weather'][0]['description']
    region = Region(region_id=data['id'])
    region.save()
    current_weather =  Weather(region_id=region, region=data['name'], temperature=temp,
    cloud_desc=cloud_desc, wind_speed=wind_range_check(data['wind']['speed']), datetime=date_time)
    current_weather.save()
    log.info('Database updated')

def wind_range_check(speed):
    wind_speed_check = {range(0,1):'Calm', range(1,6):'Light air', range(6,12):'Light breeze',
    range(12,20):'Gentle breeze', range(20,29):'Moderate breeze', range(29,39):'Fresh breeze', range(39,40):'Strong breeze',range(40,60):'Strong winds',range(39,40):'Very Strong winds'}
    for k,v in wind_speed_check.items():
        if int(speed) in k:
            return v
        elif int(speed) > 40:
            return "Wind alert"
        else:
            continue
    return "Data Not found"

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(populate_weather_info, 'interval', minutes=60)
    scheduler.start()
