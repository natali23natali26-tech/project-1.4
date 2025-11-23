import pytest
from src.products import Product, Category


# ТЕСТЫ ДЛЯ КЛАССА Product

@pytest.mark.parametrize(
    "name, description, price, quantity",
    [
        ("Телефон", "Смартфон", 20000.0, 10),
        ("Ноутбук", "Игровой", 80000.5, 5),
        # Пустое имя — допустимо по текущей логике
        ("", "Без названия", 1000.0, 1),
        # Нулевое количество — допустимо
        ("Камера", "", 30000.0, 0),
    ]
)
def test_product_initialization(name, description, price, quantity):
    """Проверяет, что объект Product корректно инициализируется."""
    product = Product(name, description, price, quantity)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


# ТЕСТЫ ДЛЯ КЛАССА Category

@pytest.mark.parametrize(
    "name, description, product_count_in_list",
    [
        ("Смартфоны", "Умные телефоны", 3),
        ("Телевизоры", "Экраны большого размера", 1),
        ("Пустая категория", "Нет товаров", 0),
    ]
)
def test_category_initialization(name, description, product_count_in_list):
    """Проверяет, что объект Category корректно инициализируется."""
    # Создаём список продуктов динамически
    products = [
        Product(f"Товар_{i}", f"Описание_{i}", 1000.0, 1)
        for i in range(product_count_in_list)
    ]

    category = Category(name, description, products)

    assert category.name == name
    assert category.description == description
    assert len(category.products) == product_count_in_list
    assert category.products == products


# ТЕСТЫ СЧЁТЧИКОВ С ИСПОЛЬЗОВАНИЕМ patch

def test_category_and_product_count_incremented_correctly():
    """Проверяет, что счётчики category_count
    и product_count увеличиваются корректно."""
    # Сбрасываем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("P1",
                       "Desc",
                       1000.0,
                       5)
    product2 = Product("P2",
                       "Desc",
                       2000.0,
                       3)
    product3 = Product("P3",
                       "Desc",
                       1500.0,
                       7)

    # Создаём категории
    category1 = Category("Кат1",
                         "Описание",
                         [product1, product2])  # +1 категория, +2
