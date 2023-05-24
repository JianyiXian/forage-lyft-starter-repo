from battery.battery import Battery


class SpindlerBattery(Battery):
    def needs_service(self, year=2):
        return super().needs_service(year)
