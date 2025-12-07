from typing import List
from src.products import Product


class Category:
    """
    Класс, представляющий категорию товаров.

    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        __products (List[Product]):
        Приватный список товаров категории.

    Атрибуты класса:
        category_count (int):
        Общее количество созданных категорий.
        product_count (int):
        Общее количество уникальных товаров (по числу добавлений).
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str,
                 description: str,
                 products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию и увеличивает счётчик product_count."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер: возвращает строковое представление
        всех товаров через str(product)."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        """
        Строковое отображение категории:
        'Название категории, количество продуктов: X шт.'
        X — сумма остатков всех товаров.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self) -> str:
        return (f"Category(name='{self.name}', "
                f"products_count={len(self.__products)})")
