from abc import ABC, abstractmethod


# Реализация (имплементация)
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int):
        pass


# Конкретные реализации
class TV(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self):
        self._enabled = True
        print("TV is ON")

    def disable(self):
        self._enabled = False
        print("TV is OFF")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        self._volume = max(0, min(100, percent))
        print(f"TV volume set to {self._volume}%")


class Radio(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self):
        self._enabled = True
        print("Radio is ON")

    def disable(self):
        self._enabled = False
        print("Radio is OFF")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        self._volume = max(0, min(100, percent))
        print(f"Radio volume set to {self._volume}%")


# Абстракция
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)


# Расширенная абстракция
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.set_volume(0)
        print("Device muted")


# Демонстрация
if __name__ == "__main__":
    print("=== Basic Remote for TV ===")
    tv = TV()
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.volume_up()
    remote.volume_down()

    print("\n=== Advanced Remote for Radio ===")
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.volume_up()
    advanced_remote.mute()
    advanced_remote.toggle_power()