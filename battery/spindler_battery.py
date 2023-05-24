from battery.battery import Battery


class SpindlerBattery(Battery):
    def needs_service(self, max_year=2):
        return super().needs_service(max_year)
