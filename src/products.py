from typing import Any, Dict, List, Optional


class Product:
    """
    Класс, представляющий товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара в рублях (может включать копейки).
        quantity (int): Количество товара в наличии (в штуках).
    """

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return (
            f"Product(name='{self.name}', "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )

    @classmethod
    def new_product(
        cls,
        product_data: Dict[str, Any],
        products_list: Optional[List["Product"]] = None
    ) -> "Product":
        """
        Класс-метод для создания или обновления товара.

        Аргументы:
            product_data (dict): Словарь с данными товара.
                Пример: {
                    "name": "Телефон",
                    "description": "Смартфон",
                    "price": 20000.0,
                    "quantity": 5
                }
            products_list (list, optional):
            Список существующих товаров для проверки дубликатов.

        Возвращает:
            Product: Новый или обновлённый объект Product.
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        # Если передан список товаров — ищем дубликат по имени
        if products_list:
            for existing_product in products_list:
                if existing_product.name == name:
                    # Обновляем количество
                    existing_product.quantity += quantity
                    # Выбираем наибольшую цену
                    if price > existing_product.price:
                        existing_product.price = price
                    # Возвращаем уже существующий объект
                    return existing_product

        # Если дубликата нет — создаём новый товар
        return cls(name, description, price, quantity)
