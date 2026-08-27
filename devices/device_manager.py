class DeviceManager:
    def __init__(self):
        self.devices = {}

    def register(self, device_id: str, device_name: str):
        self.devices[device_id] = {
            "name": device_name,
            "authorized": False
        }

    def authorize(self, device_id: str):
        if device_id in self.devices:
            self.devices[device_id]["authorized"] = True
            return True
        return False

    def revoke(self, device_id: str):
        if device_id in self.devices:
            self.devices[device_id]["authorized"] = False
            return True
        return False

    def list_devices(self):
        return self.devices


devices = DeviceManager()
