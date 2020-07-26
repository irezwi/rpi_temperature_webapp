from datetime import timedelta, datetime
from statistics import mean

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View
from rest_framework import viewsets

from rpi_temperature_webapp.extras.TemperatureChartData import TemperatureChartData
from .models import Measurement
from .serializers import MeasurementSerializer


class HomeView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        last_day_data = self._get_last_day_data()
        last_day_data_scaled = last_day_data.adjust_values_count(100, 10)
        last_hour_data = self._get_last_hour_data()
        return render(request, 'charts.html', {"lastHourChartData": last_hour_data,
                                               "lastDayChartData": last_day_data_scaled,
                                               "lastHourAverageTemperature": mean(last_hour_data.values),
                                               "lastDayAverageTemperature": mean(last_day_data.values)})

    def _get_last_hour_data(self) -> TemperatureChartData:
        one_hour_ago = timezone.localtime(timezone.now() - timedelta(hours=1))
        return self._get_data_by_date(one_hour_ago)

    def _get_last_day_data(self) -> TemperatureChartData:
        one_day_ago = timezone.localtime(timezone.now() - timedelta(days=1))
        return self._get_data_by_date(one_day_ago)

    @staticmethod
    def _get_data_by_date(date: datetime) -> TemperatureChartData:
        now = timezone.localtime()
        return TemperatureChartData(date, now)


class MeasurementApiView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all().order_by('time')
    serializer_class = MeasurementSerializer


def about_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Nothing :(")
