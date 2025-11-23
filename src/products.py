from typing import List


class Product:
    """
    Класс, представляющий товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара в рублях (может включать копейки).
        quantity (int): Количество товара в наличии (в штуках).
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс, представляющий категорию товаров.

    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        products (List[Product]): Список товаров категории.

    Атрибуты класса:
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество товаров во всех категориях.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счётчики при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)
