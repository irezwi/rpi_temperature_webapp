from django.db.models import Q

from rpi_temperature_webapp.models import Measurements


class TemperatureChartData:
    def __init__(self):
        self.values = []
        self.labels = []

    def fill_with_data(self, start_date, end_date):
        for measurement in Measurements.objects.complex_filter(Q(time__gte=start_date, time__lte=end_date)):
            self.labels.append(measurement.time.strftime("%H:%M"))
            self.values.append(measurement.temperature)
