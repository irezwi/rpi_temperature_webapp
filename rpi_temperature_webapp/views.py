from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View

from rpi_temperature_webapp.extras.TemperatureChartData import TemperatureChartData


class HomeView(View):
    def get(self, request, *args, **kwargs):
        one_hour_ago = timezone.localtime(timezone.now() - timedelta(hours=1))
        one_day_ago = timezone.localtime(timezone.now() - timedelta(days=1))
        now = timezone.localtime()

        last_hour_chart_data = TemperatureChartData()
        last_hour_chart_data.fill_with_data(one_hour_ago, now)

        last_day_chart_data = TemperatureChartData()
        last_day_chart_data.fill_with_data(one_day_ago, now)

        return render(request, 'charts.html', {"lastHourChartData": last_hour_chart_data,
                                               "lastDayChartData": last_day_chart_data})
