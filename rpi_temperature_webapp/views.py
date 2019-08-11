from django.shortcuts import render
from django.views.generic import View
from django.utils.timezone import make_aware

from .models import Measurements

from datetime import datetime, timedelta

class HomeView(View):
    def get(self, request, *args, **kwargs):
        chart_labels = []
        chart_data = []
        one_hour_earlier = make_aware(datetime.now() - timedelta(hours=1))

        for measurement in Measurements.objects.filter(time__gte=one_hour_earlier):
            chart_labels.append(measurement.time.strftime("%d/%m/%Y, %H:%M:%S"))
            chart_data.append(measurement.temperature)

        return render(request, 'charts.html', {"chartData": chart_data,
                                               "chartLabels": chart_labels})
