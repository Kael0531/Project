from abc import ABC, abstractmethod

# 1. Abstraction: Abstract Base Class
class Product(ABC):
    def __init__(self, sku: str, name: str, price: float, stock: int):
        self._sku = sku          # Protected attribute
        self.name = name
        self.__price = price     # Private attribute (Encapsulation)
        self.__stock = stock     # Private attribute (Encapsulation)

    # Encapsulation: Getters and Setters
    def get_sku(self) -> str:
        return self._sku
        
    def get_stock(self) -> int:
        return self.__stock

    def set_stock(self, new_stock: int) -> None:
        if new_stock >= 0:
            self.__stock = new_stock
        else:
            raise ValueError("Stock cannot be negative!")

    def get_price(self) -> float:
        return self.__price

    # 2. Abstract method enforcing implementation in subclasses
    @abstractmethod
    def display_info(self) -> str:
        pass


# 3. Inheritance: Electronic Product inheriting from Product
class ElectronicProduct(Product):
    def __init__(self, sku: str, name: str, price: float, stock: int, voltage: str):
        super().__init__(sku, name, price, stock)
        self.voltage = voltage

    # 4. Polymorphism: Overriding the parent's abstract method
    def display_info(self) -> str:
        return f"[Electronics] SKU: {self.get_sku()} | Name: {self.name} | Voltage: {self.voltage} | Price: ${self.get_price()} | Stock: {self.get_stock()}"


# 3. Inheritance: Outdoor Product inheriting from Product
class OutdoorProduct(Product):
    def __init__(self, sku: str, name: str, price: float, stock: int, waterproof_level: str):
        super().__init__(sku, name, price, stock)
        self.waterproof_level = waterproof_level

    # 4. Polymorphism: Overriding the parent's abstract method
    def display_info(self) -> str:
        return f"[Outdoor] SKU: {self.get_sku()} | Name: {self.name} | Waterproof: {self.waterproof_level} | Price: ${self.get_price()} | Stock: {self.get_stock()}"