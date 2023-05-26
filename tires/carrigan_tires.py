from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for data in self.tire_wear:
            if data >= 0.9:
                return True
        return False
