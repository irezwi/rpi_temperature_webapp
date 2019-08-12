from datetime import datetime, timedelta
import pytz

from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views.generic import View

from rpi_temperature_webapp.extras.TemperatureChartData import TemperatureChartData


class HomeView(View):
    def get(self, request, *args, **kwargs):
        warsaw_timezone = pytz.timezone("Europe/Warsaw")
        one_hour_ago = warsaw_timezone.localize(datetime.now() - timedelta(hours=1))
        now = warsaw_timezone.localize(datetime.now())

        last_hour_chart_data = TemperatureChartData()
        last_hour_chart_data.fill_with_data(one_hour_ago, now)

        return render(request, 'charts.html', {"lastHourChartData": last_hour_chart_data})
