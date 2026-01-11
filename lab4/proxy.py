from abc import ABC, abstractmethod
import time


# Интерфейс
class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> str:
        pass


# Реальный объект
class RealDatabase(Database):
    def __init__(self):
        # Имитация тяжелой инициализации
        print("Initializing real database...")
        time.sleep(2)
        print("Database initialized!")

    def query(self, sql: str) -> str:
        return f"Executed: {sql}"


# Прокси
class DatabaseProxy(Database):
    def __init__(self):
        self._real_database = None
        self._cache = {}

    def query(self, sql: str) -> str:
        # Ленивая инициализация
        if self._real_database is None:
            self._real_database = RealDatabase()

        # Кэширование
        if sql in self._cache:
            print(f"Returning cached result for: {sql}")
            return self._cache[sql]

        # Выполнение запроса
        result = self._real_database.query(sql)
        self._cache[sql] = result
        return result

    def clear_cache(self):
        self._cache.clear()
        print("Cache cleared!")


# Демонстрация
if __name__ == "__main__":
    proxy = DatabaseProxy()

    print("\n=== First query (will initialize database) ===")
    print(proxy.query("SELECT * FROM users"))

    print("\n=== Same query again (will use cache) ===")
    print(proxy.query("SELECT * FROM users"))

    print("\n=== New query ===")
    print(proxy.query("SELECT * FROM orders"))

    print("\n=== Clear cache ===")
    proxy.clear_cache()

    print("\n=== Query after cache clear ===")
    print(proxy.query("SELECT * FROM users"))