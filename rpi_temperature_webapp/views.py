from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views.generic import View

from rpi_temperature_webapp.lib.TemperatureChartData import TemperatureChartData
from .models import Measurements


class HomeView(View):
    def get(self, request, *args, **kwargs):
        one_day_ago = make_aware(datetime.now() - timedelta(days=1))
        one_hour_ago = make_aware(datetime.now() - timedelta(hours=1))
        now = make_aware(datetime.now())

        last_hour_chart_data = TemperatureChartData()
        last_hour_chart_data.fill_with_data(one_hour_ago, now)

        return render(request, 'charts.html', {"lastHourChartData": last_hour_chart_data})
