from typing import Any, Dict, List, Optional


class Product:
    """
    Класс, представляющий товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        __price (float): Приватная цена товара.
        quantity (int): Количество товара в наличии.
    """

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = 0.0
        # Используем сеттер для валидации
        self.price = price  # вызовет сеттер

    @property
    def price(self) -> float:
        """Геттер для цены. """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __repr__(self) -> str:
        return (f"Product(name='{self.name}', "
                f"price={self.price}, "
                f"quantity={self.quantity})")

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

        return cls(name, description, price, quantity)
