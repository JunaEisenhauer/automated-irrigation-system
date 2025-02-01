from prometheus_client import CollectorRegistry, Gauge, start_http_server


class PrometheusClient:
    def __init__(self):
        registry = CollectorRegistry()
        self._humidity = Gauge("humidity", "Humidity")
        registry.register(self._humidity)
        self._pump = Gauge("pump", "Pump state")
        registry.register(self._pump)

    def start_server(self):
        start_http_server(9110)

    def update_humidity(self, humidity: float):
        self._humidity.set(humidity)

    def update_pump_state(self, pump_state: bool):
        self._pump.set(pump_state)
