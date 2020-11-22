from django.db.models import Q
from datetime import datetime
from typing import List

from rpi_temperature_webapp.models import Measurement


class TemperatureChartData:
    def __init__(self, start_date: datetime, end_date: datetime) -> None:
        self.units = "C"
        self.labels: List[str] = list()
        self.values: List[float] = list()

        measurements: List[Measurement] = Measurement.objects.complex_filter(Q(time__gte=start_date,
                                                                               time__lte=end_date))
        for measurement in measurements:
            self.labels.append(measurement.time.strftime("%H:%M"))
            self.values.append(measurement.temperature)

    def adjust_values_count(self, max_count: int, step: int):
        if len(self.values) > max_count:
            self.labels = self.labels[::step]
            self.values = self.values[::step]
        return self

    def scale_temperatures_to_K(self) -> None:
        if self.units == "C":
            self.values = [value + 273.15 for value in self.values]

    def scale_temperatures_to_C(self) -> None:
        if self.units == "K":
            self.values = [value - 273.15 for value in self.values]
