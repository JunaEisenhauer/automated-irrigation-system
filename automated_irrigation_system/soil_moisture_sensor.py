from gpiozero import MCP3008


class SensorCalibration:
    def __init__(self, offline_offset: float, gradient: float, offset: float):
        self.offline_offset = offline_offset
        self.gradient = gradient
        self.offset = offset

    def calibrate_linear(self, value: float) -> float:
        return self.gradient * value + self.offset


class SoilMoistureSensor:
    def __init__(self, channel: bytes, device: bytes, calibration: SensorCalibration):
        self._adc = MCP3008(channel=channel, device=device)
        self.calibration = calibration

    def read(self) -> float:
        data = self._adc.value

        if data <= self.calibration.offline_offset:
            return -1

        return self.calibration.calibrate_linear(1 - data)
