from engine.engine import Engine


class CapuletEngine(Engine):

    def needs_service(self, max_mileage=30000):
        return super().needs_service(max_mileage)
