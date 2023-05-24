from engine.engine import Engine


class WilloughbyEngine(Engine):
    def engine_should_be_serviced(self, max_mileage=60000):
        return super().needs_service(max_mileage)
