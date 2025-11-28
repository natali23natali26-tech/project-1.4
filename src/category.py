from typing import List
from src.products import Product


class Category:
    """
    Класс, представляющий категорию товаров.

    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        __products (List[Product]): Приватный список товаров категории.

    Атрибуты класса:
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество товаров во всех категориях.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str,
                 description: str,
                 products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = []  # Приватный список

        Category.category_count += 1

        # Добавляем товары через add_product
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в приватный список __products.
        Увеличивает счётчик product_count.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Геттер: возвращает список товаров (только для чтения)."""
        return self.__products

    def __repr__(self) -> str:
        return (f"Category(name='{self.name}', "
                f"products_count={len(self.__products)})")
