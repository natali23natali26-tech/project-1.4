from typing import Any, Dict, List, Optional


class Product:
    """
    Класс, представляющий товар.
    """
    def __init__(self, name: str, description: str,
                 price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = 0.0
        self.price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self) -> str:
        return (f"{self.name}, {int(self.price)} руб. "
                f"Остаток: {self.quantity} шт.")

    def __repr__(self) -> str:
        return (f"Product(name='{self.name}', "
                f"price={self.price}, quantity={self.quantity})")

    @classmethod
    def new_product(
        cls,
        product_data: Dict[str, Any],
        products_list: Optional[List["Product"]] = None,
    ) -> "Product":
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if products_list:
            for existing_product in products_list:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product
            new_product = cls(name, description, price, quantity)
            products_list.append(new_product)
            return new_product
        return cls(name, description, price, quantity)

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только продукты (Product).")
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать товары разных типов: "
                            f"{type(self).__name__} и {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __radd__(self, other: float) -> float:
        if isinstance(other, (int, float)):
            return other + (self.price * self.quantity)
        return NotImplemented


class Smartphone(Product):
    """
    Класс смартфона.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float | str,  # ← современный синтаксис | вместо Union
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = str(efficiency)  # всегда храним как строку
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self) -> str:
        return (f"Smartphone(name='{self.name}', "
                f"price={self.price}, "
                f"quantity={self.quantity}, "
                f"efficiency='{self.efficiency}', "
                f"model='{self.model}', "
                f"memory={self.memory}, "
                f"color='{self.color}')")


class LawnGrass(Product):
    """
    Класс газонной травы.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self) -> str:
        return (f"LawnGrass(name='{self.name}', "
                f"price={self.price}, "
                f"quantity={self.quantity}, "
                f"country='{self.country}', "
                f"germination_period='{self.germination_period}', "
                f"color='{self.color}')")
