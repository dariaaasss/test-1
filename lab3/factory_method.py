from abc import ABC, abstractmethod


# Абстрактный класс транспорта
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# Конкретные классы транспорта
class Truck(Transport):
    def deliver(self):
        return "Доставка грузовиком по земле"


class Ship(Transport):
    def deliver(self):
        return "Доставка кораблем по морю"


# Абстрактный создатель
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()


# Конкретные создатели
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


# Демонстрация
if __name__ == "__main__":
    road_logistics = RoadLogistics()
    sea_logistics = SeaLogistics()

    print(road_logistics.plan_delivery())
    print(sea_logistics.plan_delivery())