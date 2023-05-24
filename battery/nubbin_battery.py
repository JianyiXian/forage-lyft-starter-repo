from battery.battery import Battery


class NubbinBattery(Battery):
    def needs_service(self, year=3):
        return super().needs_service(year)
