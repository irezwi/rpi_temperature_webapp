from django.db.models import Q

from rpi_temperature_webapp.models import Measurements


class TemperatureChartData:
    def __init__(self):
        self.values = []
        self.labels = []
        self.units = "C"

    def fill_with_data(self, start_date, end_date):
        for measurement in Measurements.objects.complex_filter(Q(time__gte=start_date, time__lte=end_date)):
            self.labels.append(measurement.time.strftime("%H:%M"))
            self.values.append(measurement.temperature)

    def scale_temperatures_to_K(self):
        if self.units == "C":
            self.values = [value + 273.15 for value in self.values]
        elif self.units == "K":
            pass

    def scale_temperatures_to_C(self):
        if self.units == "C":
            pass
        elif self.units == "K":
            self.values = [value - 273.15 for value in self.values]
