class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}"


# Абстрактный строитель
class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    def build_gpu(self):
        self.computer.gpu = "Integrated"

    def get_computer(self):
        return self.computer


# Конкретные строители
class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel i9"

    def build_ram(self):
        self.computer.ram = "32GB DDR5"

    def build_storage(self):
        self.computer.storage = "2TB NVMe SSD"

    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"


class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel i5"

    def build_ram(self):
        self.computer.ram = "16GB DDR4"

    def build_storage(self):
        self.computer.storage = "512GB SSD"


# Директор
class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()
        return self.builder.get_computer()


# Демонстрация
if __name__ == "__main__":
    # Создание игрового компьютера
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    gaming_pc = director.build_computer()
    print("Gaming PC:", gaming_pc)

    # Создание офисного компьютера
    office_builder = OfficeComputerBuilder()
    director.builder = office_builder
    office_pc = director.build_computer()
    print("Office PC:", office_pc)