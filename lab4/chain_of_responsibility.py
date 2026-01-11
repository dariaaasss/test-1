from abc import ABC, abstractmethod


# Обработчик
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> str:
        pass

    def _handle_next(self, request: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return f"Request '{request}' was not handled"


# Конкретные обработчики
class TechnicalSupportHandler(Handler):
    def handle(self, request: str) -> str:
        if "technical" in request.lower() or "bug" in request.lower():
            return f"Technical Support handled: {request}"
        else:
            return self._handle_next(request)


class BillingSupportHandler(Handler):
    def handle(self, request: str) -> str:
        if "billing" in request.lower() or "payment" in request.lower():
            return f"Billing Support handled: {request}"
        else:
            return self._handle_next(request)


class GeneralSupportHandler(Handler):
    def handle(self, request: str) -> str:
        if "question" in request.lower() or "help" in request.lower():
            return f"General Support handled: {request}"
        else:
            return self._handle_next(request)


class ManagerHandler(Handler):
    def handle(self, request: str) -> str:
        if "complaint" in request.lower() or "manager" in request.lower():
            return f"Manager handled: {request}"
        else:
            return self._handle_next(request)


# Демонстрация
if __name__ == "__main__":
    # Создаем цепочку
    technical = TechnicalSupportHandler()
    billing = BillingSupportHandler()
    general = GeneralSupportHandler()
    manager = ManagerHandler()

    # Настраиваем порядок обработки
    technical.set_next(billing).set_next(general).set_next(manager)

    # Тестируем запросы
    requests = [
        "I have a technical bug in the app",
        "My payment was declined",
        "I just have a general question",
        "I want to file a complaint",
        "I need some help"
    ]

    for request in requests:
        print(f"\nRequest: {request}")
        print(f"Response: {technical.handle(request)}")