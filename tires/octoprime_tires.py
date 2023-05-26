from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        sum_ware = 0
        for data in self.tire_wear:
            sum_ware += data
        return sum_ware > 3
