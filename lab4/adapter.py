# Целевой интерфейс
class EuropeanSocket:
    def voltage(self) -> int:
        return 230

    def plug_type(self) -> str:
        return "Type F (Schuko)"

    def description(self) -> str:
        return f"European Socket: {self.voltage()}V, {self.plug_type()}"


# Адаптируемый класс (американская розетка)
class AmericanSocket:
    def us_voltage(self) -> int:
        return 120

    def us_plug_type(self) -> str:
        return "Type A/B"

    def us_description(self) -> str:
        return f"US Socket: {self.us_voltage()}V, {self.us_plug_type()}"


# Адаптер
class SocketAdapter(EuropeanSocket):
    def __init__(self, american_socket: AmericanSocket):
        self._american_socket = american_socket
        self._voltage_converter = 230 / 120  # Конвертер напряжения

    def voltage(self) -> int:
        # Адаптируем напряжение
        return int(self._american_socket.us_voltage() * self._voltage_converter)

    def plug_type(self) -> str:
        # Адаптируем тип вилки
        us_type = self._american_socket.us_plug_type()
        return f"Adapter for {us_type} to Type F"

    def original_description(self) -> str:
        return self._american_socket.us_description()


# Европейское устройство
class EuropeanDevice:
    def __init__(self, name: str, socket: EuropeanSocket):
        self.name = name
        self.socket = socket

    def plug_in(self):
        return f"{self.name} plugged into {self.socket.description()}"


# Демонстрация
if __name__ == "__main__":
    print("=== European device in Europe ===")
    european_socket = EuropeanSocket()
    laptop = EuropeanDevice("Laptop", european_socket)
    print(laptop.plug_in())

    print("\n=== European device in USA (using adapter) ===")
    american_socket = AmericanSocket()
    adapter = SocketAdapter(american_socket)
    laptop_in_usa = EuropeanDevice("Laptop", adapter)
    print(f"Original: {adapter.original_description()}")
    print(laptop_in_usa.plug_in())

    # Дополнительный пример с другим устройством
    print("\n=== Another device ===")
    phone_charger = EuropeanDevice("Phone Charger", adapter)
    print(f"Original: {adapter.original_description()}")
    print(phone_charger.plug_in())