from datetime import datetime, timedelta
import pytz

from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils import timezone
from django.views.generic import View

from rpi_temperature_webapp.extras.TemperatureChartData import TemperatureChartData


class HomeView(View):
    def get(self, request, *args, **kwargs):
        one_hour_ago = timezone.localtime(timezone.now() - timedelta(hours=1))
        now = timezone.localtime()

        last_hour_chart_data = TemperatureChartData()
        last_hour_chart_data.fill_with_data(one_hour_ago, now)

        return render(request, 'charts.html', {"lastHourChartData": last_hour_chart_data,
                                               "startDate": str(one_hour_ago)})
