import pytest
from src.products import Product
from src.category import Category
from unittest.mock import patch


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


# Тестирование для Category

@pytest.mark.parametrize(
    "cat_name, cat_description, product_count_in_list",
    [
        ("Смартфоны", "Умные телефоны", 3),
        ("Телевизоры", "Экраны большого размера", 1),
        ("Пустая категория", "Нет товаров", 0),
    ]
)
def test_category_initialization(cat_name,
                                 cat_description,
                                 product_count_in_list):
    """Проверяет, что объект Category корректно инициализируется."""
    # Создаём список продуктов динамически
    products = [
        Product(f"Товар_{i}", f"Описание_{i}", 1000.0, 1)
        for i in range(product_count_in_list)
    ]

    category = Category(cat_name, cat_description, products)

    # Проверяем основные атрибуты
    assert category.name == cat_name
    assert category.description == cat_description

    # Проверяем количество товаров через строковое представление
    if product_count_in_list == 0:
        assert category.products == ""
    else:
        lines = category.products.strip().split("\n")
        assert len(lines) == product_count_in_list


# тестирование счетчиков с использованием patch
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


# Тест для new_product — создание и обновление дубликата
def test_new_product_creates_and_updates():
    """Проверяет, что new_product создаёт новый товар
    или обновляет существующий."""
    # Создаём список товаров
    existing_product = Product("Телефон",
                               "Смартфон",
                               20000.0, 5)
    products = [existing_product]

    # Новый товар с тем же именем, но большей ценой и количеством
    new_data = {
        "name": "Телефон",
        "description": "Обновлённая модель",
        "price": 25000.0,
        "quantity": 3,
    }

    result = Product.new_product(new_data, products)

    # Должен вернуться существующий объект
    assert result is existing_product
    assert result.quantity == 8  # 5 + 3
    assert result.price == 25000.0  # обновилось на большую цену


# Тест для геттера products в Category
def test_category_products_property():
    """Проверяет, что геттер products возвращает строку в нужном формате."""
    product1 = Product("Телефон", "Смартфон",
                       20000.5, 5)
    product2 = Product("Ноутбук", "Игровой",
                       80000.0, 1)

    category = Category("Электроника",
                        "Цифровые устройства",
                        [product1, product2])

    expected = ("Телефон, 20000 руб. Остаток: 5 шт."
                "\nНоутбук, 80000 руб. Остаток: 1 шт.")
    assert category.products == expected


# Тест для сеттера price
def test_product_price_setter():
    """Проверяет, что сеттер цены не позволяет установить
    ноль или отрицательное значение."""
    product = Product("Тест", "Описание",
                      1000.0, 10)

    # Проверяем, что цена установилась
    assert product.price == 1000.0

    # Пробуем установить отрицательную цену
    with patch("builtins.print") as mock_print:
        product.price = -500
        mock_print.assert_called_with("Цена не должна быть "
                                      "нулевая или отрицательная")
        assert product.price == 1000.0  # цена не изменилась

    # Пробуем установить ноль
    with patch("builtins.print") as mock_print:
        product.price = 0
        mock_print.assert_called_with("Цена не должна быть "
                                      "нулевая или отрицательная")
        assert product.price == 1000.0

    # Устанавливаем корректную цену
    product.price = 1500.0
    assert product.price == 1500.0
