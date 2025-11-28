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

    # Явная аннотация типа для приватного атрибута
    __products: list[Product]

    def __init__(self, name: str,
                 description: str,
                 products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = []  # Теперь тип известен

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
    def products(self) -> str:
        """
        Геттер: возвращает строковое представление всех товаров в категории.
        Каждый товар — в формате:
        Название продукта, 80 руб. Остаток: 15 шт.

        Возвращает:
            str: Многострочная строка с информацией о товарах.
                 Если товаров нет — пустая строка.
        """
        if not self.__products:
            return ""

        product_lines = [
            (f"{product.name}, "
             f"{int(product.price)} руб. "
             f"Остаток: {product.quantity} шт.")
            for product in self.__products
        ]

        return "\n".join(product_lines)

    def __repr__(self) -> str:
        return (f"Category(name='{self.name}', "
                f"products_count={len(self.__products)})")
