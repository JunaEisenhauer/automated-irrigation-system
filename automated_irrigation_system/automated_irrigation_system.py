from prometheus_connection import PrometheusClient
from pump import Pump
from soil_moisture_sensor import SoilMoistureSensor, SensorCalibration

HUMIDITY_TO_START_PUMP = 65
HUMIDITY_TO_STOP_PUMP = 75


def main():
    calibration = SensorCalibration(offline_offset=0.1, gradient=238.0564729962321, offset=-76.87816904684377)
    sensor = SoilMoistureSensor(channel=0, device=1, calibration=calibration)
    pump = Pump(gpio=23)
    prometheus = PrometheusClient()
    prometheus.start_server()

    while True:
        humidity = min(max(sensor.read(), 0), 100)
        prometheus.update_humidity(humidity)
        if humidity <= HUMIDITY_TO_START_PUMP:
            pump.start()
            prometheus.update_pump_state(True)
        elif humidity >= HUMIDITY_TO_STOP_PUMP:
            pump.stop()
            prometheus.update_pump_state(False)


if __name__ == '__main__':
    main()
