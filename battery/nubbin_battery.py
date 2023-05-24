from battery.battery import Battery


class NubbinBattery(Battery):
    def needs_service(self, max_year=4):
        return super().needs_service(max_year)
