from abc import ABC, abstractmethod


# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass


# Конкретные продукты для Windows
class WindowsButton(Button):
    def click(self):
        return "Windows button clicked"


class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows checkbox checked"


# Конкретные продукты для Mac
class MacButton(Button):
    def click(self):
        return "Mac button clicked"


class MacCheckbox(Checkbox):
    def check(self):
        return "Mac checkbox checked"


# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Демонстрация
if __name__ == "__main__":
    def create_ui(factory: GUIFactory):
        button = factory.create_button()
        checkbox = factory.create_checkbox()

        print(button.click())
        print(checkbox.check())


    print("Windows UI:")
    create_ui(WindowsFactory())

    print("\nMac UI:")
    create_ui(MacFactory())