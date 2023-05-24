from abc import ABC
from datetime import datetime


class Battery(ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self, max_year):
        return self.current_date.year - self.last_service_date.year > max_year
