from abc import ABC


class Engine(ABC):
    def __init__(self, last_service_mileage, current_milage):
        self.last_service_mileage = last_service_mileage
        self.current_milage = current_milage

    def needs_service(self, max_mileage):
        return self.current_milage - self.last_service_mileage > max_mileage
