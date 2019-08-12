from datetime import datetime, timedelta
import pytz

from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views.generic import View

from rpi_temperature_webapp.extras.TemperatureChartData import TemperatureChartData


class HomeView(View):
    def get(self, request, *args, **kwargs):
        warsaw_timezone = pytz.timezone('Europe/Warsaw')
        one_hour_ago = datetime.now(warsaw_timezone) - timedelta(hours=1)
        now = datetime.now(warsaw_timezone)

        last_hour_chart_data = TemperatureChartData()
        last_hour_chart_data.fill_with_data(one_hour_ago, now)

        return render(request, 'charts.html', {"lastHourChartData": last_hour_chart_data})
